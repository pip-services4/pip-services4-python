# -*- coding: utf-8 -*-
from typing import Optional, List

import pymemcache
from pip_services4_commons.errors import ConfigException, InvalidStateException
from pip_services4_components.config import IConfigurable, ConfigParams
from pip_services4_components.context import IContext, ContextResolver
from pip_services4_components.refer import IReferenceable, IReferences
from pip_services4_components.run import IOpenable
from pip_services4_config.connect import ConnectionResolver
from pip_services4_logic.lock import Lock


class MemcachedLock(Lock, IConfigurable, IReferenceable, IOpenable):
    """
    Distributed lock that implemented based on Memcaches caching service.

    The current implementation does not support authentication.

    ### Configuration parameters ###

        - connection(s):
            - discovery_key:         (optional) a key to retrieve the connection from :class:`IDiscovery <pip_services4_config.connect.IDiscovery.IDiscovery>`
            - host:                  host name or IP address
            - port:                  port number
            - uri:                   resource URI or connection string with all parameters in it
        - options:
            - retry_timeout:         timeout in milliseconds to retry lock acquisition. (Default: 100)
            - max_size:              maximum number of values stored in this cache (default: 1000)
            - max_key_size:          maximum key length (default: 250)
            - max_expiration:        maximum expiration duration in milliseconds (default: 2592000)
            - max_value:             maximum value length (default: 1048576)
            - pool_size:             pool size (default: 5)
            - reconnect:             reconnection timeout in milliseconds (default: 10 sec)
            - retries:               number of retries (default: 3)
            - timeout:               default caching timeout in milliseconds (default: 1 minute)
            - failures:              number of failures before stop retrying (default: 5)
            - retry:                 retry timeout in milliseconds (default: 30 sec)
            - idle:                  idle timeout before disconnect in milliseconds (default: 5 sec)

    ### References ###

        - `*:discovery:*:*:1.0`      (optional) :class:`IDiscovery <pip_services4_config.connect.IDiscovery.IDiscovery>` services to resolve connection

    Example:

    .. code-block:: python

        lock = MemcachedLock()
        lock.configure(ConfigParams.from_tuples(
            "connection.host", "localhost",
            "connection.port", 11211
        ))
        
        lock.open(Context.from_trace_id("123"))
        lock.acquire_lock(Context.from_trace_id("123"), "key1", 3000, 1000)
        try:
            # Processing...
            pass
        finally:
            lock.release_lock(Context.from_trace_id("123"), "key1")
        
    """

    def __init__(self):
        """
        Creates a new instance of this cache.
        """
        self.__connection_resolver: ConnectionResolver = ConnectionResolver()

        # self.__max_key_size: int = 250
        # self.__max_expiration: int = 2592000
        # self.__max_value: int = 1048576
        self.__pool_size: int = 5
        self.__reconnect: int = 10000
        self.__timeout: int = 5000
        self.__retries: int = 5
        self.__failures: int = 5
        self.__retry: int = 30000
        # self.__remove: bool = False
        self.__idle: int = 5000

        self.__client: pymemcache.HashClient = None

    def configure(self, config: ConfigParams):
        """
        Configures component by passing configuration parameters.

        :param config: configuration parameters to be set.
        """
        self.__connection_resolver.configure(config)

        # self.__max_key_size = config.get_as_integer_with_default('options.max_key_size', self.__max_key_size)
        # self.__max_expiration = config.get_as_integer_with_default('options.max_expiration', self.__max_expiration)
        # self.__max_value = config.get_as_integer_with_default('options.max_value', self.__max_value)
        self.__pool_size = config.get_as_integer_with_default('options.pool_size', self.__pool_size)
        self.__reconnect = config.get_as_integer_with_default('options.reconnect', self.__reconnect)
        self.__timeout = config.get_as_integer_with_default('options.timeout', self.__timeout)
        self.__retries = config.get_as_integer_with_default('options.retries', self.__retries)
        self.__failures = config.get_as_integer_with_default('options.failures', self.__failures)
        self.__retry = config.get_as_integer_with_default('options.retry', self.__retry)
        # self.__remove = config.get_as_integer_with_default('options.remove', self.__remove)
        self.__idle = config.get_as_integer_with_default('options.idle', self.__idle)

    def set_references(self, references: IReferences):
        """
        Sets references to dependent components.

        :param references: references to locate the component dependencies.
        """
        self.__connection_resolver.set_references(references)

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
        connections = self.__connection_resolver.resolve_all(context)
        if len(connections) == 0:
            raise ConfigException(
                ContextResolver.get_trace_id(context),
                'NO_CONNECTION',
                'Connection is not configured'
            )

        servers: List[str] = []
        for connection in connections:
            host = connection.get_host()
            port = connection.get_port() or 11211
            servers.append(f'{host}:{port}')

        options = {
            # TODO: this options have not support by driver, but can execute by cmd driver method
            # 'maxKeySize': self.__max_key_size,
            # 'maxExpiration': self.__max_expiration,
            # 'maxValue': self.__max_value, # driver don't have this config
            # 'retries': self.__retries,
            # 'remove': self.__remove,
            'retry_attempts': self.__failures,  # driver automatically remove dead servers from the pool (by attemps)
            'max_pool_size': self.__pool_size,
            'connect_timeout': self.__reconnect / 1000,
            'timeout': self.__timeout / 1000,
            'retry_timeout': self.__retry / 1000,
            'pool_idle_timeout': self.__idle / 1000,
            'default_noreply': False
        }

        self.__client = pymemcache.HashClient(servers=servers, **options)

    def close(self, correlation_id: Optional[str]):
        """
        Closes component and frees used resources.

        :param correlation_id: (optional) transaction id to trace execution through call chain.
        """
        self.__client.quit()
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
        :return: `true` if lock was successfull and `false` otherwise.
        """
        self.__check_opened(context)

        lifetime_in_sec = int(ttl / 1000)

        result = self.__client.add(key, 'lock', lifetime_in_sec)
        return result is True

    def release_lock(self, context: Optional[IContext], key: str):
        """
        Releases prevously acquired lock by its key.

        :param context: (optional) transaction id to trace execution through call chain.
        :param key: a unique lock key to release.
        """
        self.__check_opened(context)

        return self.__client.delete(key)
