# -*- coding: utf-8 -*-

from typing import List, Optional, Any

from pip_services4_commons.errors import ConfigException
from pip_services4_components.config import IConfigurable, ConfigParams
from pip_services4_components.context import IContext, ContextResolver
from pip_services4_components.refer import IReferenceable, IReferences
from pip_services4_components.run import IOpenable
from pip_services4_config.auth import CredentialResolver, CredentialParams
from pip_services4_config.connect import ConnectionResolver, ConnectionParams


class SqlServerConnectionResolver(IReferenceable, IConfigurable, IOpenable):
    """
    Helper class that resolves SqlServer connection and credential parameters,
    validates them and generates a connection URI.

    It is able to process multiple connections to SqlServer cluster nodes.

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
        self._connection_resolver.set_references(references)

    def __validate_connection(self, context: Optional[IContext], connection: ConnectionParams) -> Any:
        uri = connection.get_uri()
        if uri is not None:
            return None

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

        return None

    def __validate_connections(self, context: Optional[IContext], connections: List[ConnectionParams]) -> Any:
        if connections is None or len(connections) == 0:
            raise ConfigException(ContextResolver.get_trace_id(context), "NO_CONNECTION",
                                  "Database connection is not set")

        for connection in connections:
            self.__validate_connection(context, connection)

        return None

    def __compose_uri(self, connections: List[ConnectionParams], credential: CredentialParams) -> str:
        # If there is a uri then return it immediately
        for connection in connections:
            uri = connection.get_uri()
            if uri:
                return uri

        hosts = ''
        for connection in connections:
            host = connection.get_host()
            port = connection.get_port()

            if len(hosts) > 0:
                hosts += ','
            hosts += host + ('' if port is None else f':{port}')

        # Define database
        database = ''

        for connection in connections:
            database = database or connection.get_as_nullable_string('database')

        if len(database) > 0:
            database = '/' + database

        # Define authentication part
        auth = ''
        if credential:
            username = credential.get_username()
            if username:
                password = credential.get_password()
                if password:
                    auth = username + ':' + password + '@'
                else:
                    auth = username + '@'

        # Define additional parameters parameters
        options = ConfigParams.merge_configs(*connections).override(credential)
        options.remove('uri')
        options.remove('host')
        options.remove('port')
        options.remove('database')
        options.remove('username')
        options.remove('password')

        params = ''
        keys = options.get_keys()
        for key in keys:
            if len(params) > 0:
                params += '&'

            params += key

            value = options.get_as_string(key)
            if value is not None:
                params += '=' + value

        if len(params) > 0:
            params = '?' + params

        # Compose uri
        uri = "mssql://" + auth + hosts + database + params

        return uri

    def resolve(self, context: Optional[IContext]) -> str:
        """
        Resolves SQLServer config from connection and credential parameters.

        :param context: (optional) transaction id to trace execution through call chain.
        :return: receives resolved connection uri or raise error
        """
        connections = self._connection_resolver.resolve_all(context)
        # Validate connections
        self.__validate_connections(context, connections)

        credential = self._credential_resolver.lookup(context)

        uri = self.__compose_uri(connections, credential)

        return uri
