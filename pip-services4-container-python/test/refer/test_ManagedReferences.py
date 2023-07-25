# -*- coding: utf-8 -*-
"""
    test.refer.test_ManagedReferences
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Tests for managed references
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_components.refer import Descriptor
from pip_services4_observability.log import DefaultLoggerFactory

from pip_services4_container.refer import ManagedReferences


class TestManagedReferences():

    def test_autocreate_component(self):
        refs = ManagedReferences()

        factory = DefaultLoggerFactory()
        refs.put(None, factory)

        logger = refs.get_one_required(Descriptor("*", "logger", "*", "*", "*"))
        assert None != logger

    def test_string_locator(self):
        refs = ManagedReferences()

        factory = DefaultLoggerFactory()
        refs.put(None, factory)

        component = refs.get_one_optional("ABC")
        assert None == component

    def test_null_locator(self):
        refs = ManagedReferences()

        factory = DefaultLoggerFactory()
        refs.put(None, factory)

        component = refs.get_one_optional(None)
        assert None == component
