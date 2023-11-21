# -*- coding: utf-8 -*-
from typing import Optional

import redis
from pip_services4_commons.errors import ConfigException, InvalidStateException
from pip_services4_components.config import IConfigurable, ConfigParams
from pip_services4_components.context import IContext, ContextResolver
from pip_services4_components.refer import IReferenceable, IReferences
from pip_services4_components.run import IOpenable
from pip_services4_config.auth import CredentialResolver
from pip_services4_config.connect import ConnectionResolver
from pip_services4_data.keys import IdGenerator
from pip_services4_logic.lock import Lock


class RedisLock(Lock, IConfigurable, IReferenceable, IOpenable):
    """
    Distributed lock that is implemented based on Redis in-memory database.

    ### Configuration parameters ###

        - connection(s):
            - discovery_key:         (optional) a key to retrieve the connection from :class:`IDiscovery <pip_services4_components.connect.IDiscovery.IDiscovery>`
            - host:                  host name or IP address
            - port:                  port number
            - uri:                   resource URI or connection string with all parameters in it
        - credential(s):
            - store_key:             key to retrieve parameters from credential store
            - username:              user name (currently is not used)
            - password:              user password
        - options:
            - retry_timeout:         timeout in milliseconds to retry lock acquisition. (Default: 100)
            - retries:               number of retries (default: 3)

    ### References ###

    - `*:discovery:*:*:1.0`        (optional) :class:`IDiscovery <pip_services4_components.connect.IDiscovery.IDiscovery>` services to resolve connection
    - `*:credential-store:*:*:1.0` (optional) Credential stores to resolve credential

    Example:

    .. code-block:: python

        lock = RedisLock()
        lock.configure(ConfigParams.from_tuples(
            "host", "localhost",
            "port", 6379
        ))

        lock.open(context)

        lock.acquire_lock(context, "key1", 3000, 1000)
        try:
            # Processing...
            pass
        finally:
            lock.release_lock(context, "key1")

        
    """

    def __init__(self):
        super().__init__()

        self.__connection_resolver: ConnectionResolver = ConnectionResolver()
        self.__credential_resolver: CredentialResolver = CredentialResolver()

        self.__lock: str = IdGenerator.next_long()
        self.__timeout: int = 30000
        self.__retries: int = 3
        self.__client: redis.Redis = None

    def configure(self, config: ConfigParams):
        """
        Configures component by passing configuration parameters.

        :param config: configuration parameters to be set.
        """
        self.__connection_resolver.configure(config)
        self.__credential_resolver.configure(config)

        self.__timeout = config.get_as_integer_with_default('options.timeout', self.__timeout)
        self.__retries = config.get_as_integer_with_default('options.retries', self.__retries)

    def set_references(self, references: IReferences):
        """
        Sets references to dependent components.

        :param references: references to locate the component dependencies.
        """
        self.__connection_resolver.set_references(references)
        self.__credential_resolver.set_references(references)

    def is_open(self) -> bool:
        """
        Checks if the component is opened.

        :return: true if the component has been opened and false otherwise.
        """
        return self.__client is not None

    def open(self, context: Optional[IContext]):
        """
        Opens the component.

        :param context: (optional) transaction id to trace execution through call chain.
        """
        connection = self.__connection_resolver.resolve(context)
        if connection is None:
            raise ConfigException(
                ContextResolver.get_trace_id(context),
                'NO_CONNECTION',
                'Connection is not configured'
            )

        credential = self.__credential_resolver.lookup(context)

        options = {
            # connect_timeout: self.__timeout,
            # max_attempts: self.__retries,
            'retry_on_timeout': True,
        }

        if connection.get_uri():
            options['url'] = connection.get_uri()
        else:
            options['host'] = connection.get_host() or 'localhost'
            options['port'] = connection.get_port() or 6379

        if credential is not None:
            options['password'] = credential.get_password()

        self.__client = redis.Redis(**options)

    def close(self, context: Optional[IContext]):
        """
        Closes component and frees used resources.

        :param context: (optional) transaction id to trace execution through call chain.
        """
        if self.__client is None: return

        self.__client.client()
        self.__client = None

    def __check_opened(self, context: Optional[IContext]):
        if not self.is_open():
            raise InvalidStateException(
                ContextResolver.get_trace_id(context),
                'NOT_OPENED',
                'Connection is not opened'
            )

    def try_acquire_lock(self, context: Optional[IContext], key: str, ttl: int) -> bool:
        """
        Makes a single attempt to acquire a lock by its key.
        It returns immediately a positive or negative result.

        :param context: (optional) transaction id to trace execution through call chain.
        :param key: a unique lock key to acquire.
        :param ttl: a lock timeout (time to live) in milliseconds.
        :return: `true` if lock was successfully acquired and `false` otherwise.
        """
        self.__check_opened(context)

        result = self.__client.set(name=key, value=self.__lock, nx=True, px=ttl)

        return result is True

    def release_lock(self, context: Optional[IContext], key: str):
        """
        Releases prevously acquired lock by its key.

        :param context: (optional) transaction id to trace execution through call chain.
        :param key: a unique lock key to release.
        """
        a = self.__client
        with self.__client.pipeline() as pipeline:
            # Start transaction on key
            pipeline.watch(key)

            # Read and check if lock is the same
            result = pipeline.get(key)

            if result:
                result = result.decode('utf-8')

            # Remove the lock if it matches
            if result == self.__lock:
                pipeline.multi()
                pipeline.delete(key)
                pipeline.execute()

            else:
                # Cancel transaction if it doesn't match
                pipeline.unwatch()
