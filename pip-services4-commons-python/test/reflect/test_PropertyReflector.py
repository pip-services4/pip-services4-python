# -*- coding: utf-8 -*-
"""
    tests.refer.test_PropertyReflector
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.reflect import PropertyReflector

from .StubClass import StubClass


class TestPropertyReflector:

    def test_get_property(self):
        obj = StubClass()

        value = PropertyReflector.get_property(obj, "_private_field")
        # assert None is value

        value = PropertyReflector.get_property(obj, "public_field")
        assert "ABC" == value

        value = PropertyReflector.get_property(obj, "public_prop")
        assert value is not None

    def test_get_properties(self):
        obj = StubClass()
        names = PropertyReflector.get_property_names(obj)
        # assert 2 == len(names)
        assert "public_field" in names
        assert "public_prop" in names

        map = PropertyReflector.get_properties(obj)
        # assert 2 == len(map)
        assert "ABC" == map["public_field"]
        assert None is not map["public_prop"]
