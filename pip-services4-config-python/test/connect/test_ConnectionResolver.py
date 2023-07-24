# -*- coding: utf-8 -*-
"""
    tests.auth.test_ConnectionResolver
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_components.config import ConfigParams
from pip_services4_components.context import Context
from pip_services4_components.refer import References

from pip_services4_config.connect import ConnectionResolver, ConnectionParams

RestConfig = ConfigParams.from_tuples(
    "connection.protocol", "http",
    "connection.host", "localhost",
    "connection.port", 3000
)


class TestConnectionResolver:

    def test_configure(self):
        connection_resolver = ConnectionResolver(RestConfig)
        config_list = connection_resolver.get_all()
        assert "http" == config_list[0]["protocol"]
        assert "localhost" == config_list[0]["host"]
        assert "3000" == config_list[0]["port"]

    def test_register(self):
        connection_params = ConnectionParams()
        connection_resolver = ConnectionResolver(RestConfig)

        connection_resolver.register(Context.from_trace_id("trace_id"), connection_params)
        config_list = connection_resolver.get_all()
        assert 1 == len(config_list)

        connection_params.set_discovery_key("Discovery key value")
        connection_resolver.register(Context.from_trace_id("trace_id"), connection_params)
        config_list = connection_resolver.get_all()
        assert 1 == len(config_list)

        references = References()
        connection_resolver.set_references(references)
        connection_resolver.register(Context.from_trace_id("trace_id"), connection_params)
        config_list = connection_resolver.get_all()
        assert 2 == len(config_list)
        assert "http" == config_list[0]["protocol"]
        assert "localhost" == config_list[0]["host"]
        assert "3000" == config_list[0]["port"]
        assert "Discovery key value" == config_list[1]["discovery_key"]

    def test_resolve(self):
        connection_resolver = ConnectionResolver(RestConfig)
        connection_params = connection_resolver.resolve(Context.from_trace_id("trace_id"))
        assert "http" == connection_params.get("protocol")
        assert "localhost" == connection_params.get("host")
        assert "3000" == connection_params.get("port")

        RestConfigDiscovery = ConfigParams.from_tuples(
            "connection.protocol", "http",
            "connection.host", "localhost",
            "connection.port", 3000,
            "connection.discovery_key", "Discovery key value"
        )
        references = References()
        connection_resolver = ConnectionResolver(RestConfigDiscovery, references)
        try:
            connection_params = connection_resolver.resolve(Context.from_trace_id("trace_id"))
        except Exception as ex:
            assert "Discovery wasn't found to make resolution" == ex.message
