# -*- coding: utf-8 -*-
from typing import List, Optional, Any

from pip_services4_commons.errors import ConfigException
from pip_services4_components.config import IConfigurable, ConfigParams
from pip_services4_components.context import IContext, ContextResolver
from pip_services4_components.refer import IReferenceable, IReferences
from pip_services4_config.auth import CredentialResolver, CredentialParams
from pip_services4_config.connect import ConnectionResolver, ConnectionParams


class PostgresConnectionResolver(IReferenceable, IConfigurable):
    """
    Helper class that resolves PostgreSQL connection and credential parameters,
    validates them and generates a connection URI.

    It is able to process multiple connections to PostgreSQL cluster nodes.

    ### Configuration parameters ###
        - connection(s):
            - discovery_key:               (optional) a key to retrieve the connection from :class:`IDiscovery <pip_services4_config.connect.IDiscovery.IDiscovery>`
            - host:                        host name or IP address
            - port:                        port number (default: 27017)
            - database:                    database name
            - uri:                         resource URI or connection string with all parameters in it
        - credential(s):
            - store_key:                   (optional) a key to retrieve the credentials from :class:`ICredentialStore <pip_services4_config.auth.ICredentialStore.ICredentialStore>`
            - username:                    user name
            - password:                    user password

    ### References ###
        - `*:discovery:*:*:1.0`        (optional) :class:`IDiscovery <pip_services4_config.connect.IDiscovery.IDiscovery>` services
        - `*:credential-store:*:*:1.0` (optional) :class:`ICredentialStore <pip_services4_config.auth.ICredentialStore.ICredentialStore>` stores to resolve credentials
    """

    def __init__(self):
        # The connections resolver.
        self._connection_resolver: ConnectionResolver = ConnectionResolver()
        # The credentials resolver.
        self._credential_resolver: CredentialResolver = CredentialResolver()

    def configure(self, config: ConfigParams):
        """
        Configures component by passing configuration parameters.

        :param config: configuration parameters to be set.
        """
        self._connection_resolver.configure(config)
        self._credential_resolver.configure(config)

    def set_references(self, references: IReferences):
        """
        Sets references to dependent components.

        :param references: references to locate the component dependencies.
        """
        self._connection_resolver.set_references(references)
        self._credential_resolver.set_references(references)

    def __validate_connection(self, context: Optional[IContext], connection: ConnectionParams):
        uri = connection.get_uri()
        if uri is not None:
            return

        host = connection.get_host()
        trace_id = ContextResolver.get_trace_id(context)
        if host is None:
            raise ConfigException(trace_id, "NO_HOST", "Connection host is not set")

        port = connection.get_port()
        if port == 0:
            raise ConfigException(trace_id, "NO_PORT", "Connection port is not set")

        database = connection.get_as_nullable_string('database')
        if database is None:
            raise ConfigException(trace_id, "NO_DATABASE", "Connection database is not set")

    def __validate_connections(self, context: Optional[IContext], connections: List[ConnectionParams]):
        if connections is None or len(connections) == 0:
            raise ConfigException(ContextResolver.get_trace_id(context), "NO_CONNECTION", "Database connection is not set")

        for connection in connections:
            self.__validate_connection(context, connection)

    def __compose_config(self, connections: List[ConnectionParams], credential: CredentialParams) -> Any:
        config = {}

        # Define connection part
        for connection in connections:
            uri = connection.get_uri()
            if uri:
                config['connection_string'] = uri

            host = connection.get_host()
            if host:
                config['host'] = host

            port = connection.get_port()
            if port:
                config['port'] = port

            database = connection.get_as_nullable_string('database')
            if database:
                config['dbname'] = database

        # Define authentication part
        if credential:
            username = credential.get_username()
            if username:
                config['user'] = username

            password = credential.get_password()
            if password:
                config['password'] = password

        return config

    def resolve(self, context: Optional[IContext]) -> Any:
        """
        Resolves PostgreSQL config from connection and credential parameters.

        :param context: (optional) transaction id to trace execution through call chain.
        :return: resolved connection config or raise error
        """
        connections = self._connection_resolver.resolve_all(context)
        # Validate connections
        self.__validate_connections(context, connections)

        credential = self._credential_resolver.lookup(context)
        # Credentials are not validated right now

        return self.__compose_config(connections, credential)
