# -*- coding: utf-8 -*-
"""
    test.config.test_ComponentConfig
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Tests for component configuration
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_components.config import ConfigParams
from pip_services4_components.refer import Descriptor

from pip_services4_container.config import ComponentConfig
from pip_services4_commons.reflect import TypeDescriptor
from pip_services4_commons.errors import ConfigException


class TestComponentConfig:

    def test_type(self):
        component_config = ComponentConfig()
        assert None == component_config.type

        descriptor = TypeDescriptor("new name", None)
        component_config.type = descriptor
        assert component_config.type == descriptor

    def test_descriptor(self):
        component_config = ComponentConfig()
        assert None == component_config.descriptor

        descriptor = Descriptor("group", "type", "kind", "name", "version")
        component_config.descriptor = descriptor
        assert component_config.descriptor == descriptor

    def test_config_params(self):
        component_config = ComponentConfig()
        assert None == component_config.descriptor

        config = ConfigParams.from_tuples(
            "config.key", "key",
            "config.key2", "key2"
        )
        component_config.config = config
        assert component_config.config == config

    def test_from_config(self):
        config = ConfigParams.from_tuples()
        try:
            component_config = ComponentConfig.from_config(config)
        except ConfigException as e:
            assert e.message == "Component configuration must have descriptor or type"

        config = ConfigParams.from_tuples(
            "descriptor", "descriptor_name",
            "type", "type",
            "config.key", "key",
            "config.key2", "key2"
        )
        try:
            component_config = ComponentConfig.from_config(config)
        except ConfigException as e:
            assert e.message == "Descriptor descriptor_name is in wrong format"

        descriptor = Descriptor("group", "type", "kind", "name", "version")
        tipe = TypeDescriptor("type", None)
        config = ConfigParams.from_tuples(
            "descriptor", "group:type:kind:name:version",
            "type", "type",
            "config.key", "key",
            "config.key2", "key2"
        )
        component_config = ComponentConfig.from_config(config)
        assert component_config.descriptor == descriptor
        assert component_config.type == tipe
