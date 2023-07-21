# -*- coding: utf-8 -*-
"""
    tests.refer.test_ObjectReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.data import AnyValueArray
from pip_services4_commons.data import AnyValueMap
from pip_services4_commons.reflect import ObjectReader
from .StubClass import StubClass


class TestObjectReader:

    def test_get_object_property(self):
        obj = StubClass()

        value = ObjectReader.get_property(obj, "private_field")
        assert None == value

        value = ObjectReader.get_property(obj, "public_field")
        assert "ABC" == value

        value = ObjectReader.get_property(obj, "public_prop")
        assert None != value

    def test_get_map_property(self):
        map = AnyValueMap.from_tuples(
            "key1", 123,
            "key2", "ABC"
        )

        value = ObjectReader.get_property(map, "key3")
        assert None == value

        value = ObjectReader.get_property(map, "Key1")
        assert 123 == value

        value = ObjectReader.get_property(map, "KEY2")
        assert "ABC" == value

    def test_get_array_property(self):
        array = AnyValueArray.from_values(123, "ABC")

        value = ObjectReader.get_property(array, "3")
        assert None == value

        value = ObjectReader.get_property(array, "0")
        assert 123 == value

        value = ObjectReader.get_property(array, "1")
        assert "ABC" == value

        array = [123, "ABC"]

        value = ObjectReader.get_property(array, "3")
        assert None == value

        value = ObjectReader.get_property(array, "0")
        assert 123 == value

        value = ObjectReader.get_property(array, "1")
        assert "ABC" == value

    def test_get_object_properties(self):
        obj = StubClass()
        names = ObjectReader.get_property_names(obj)
        # assert 2 == len(names)
        assert "public_field" in names
        assert "public_prop" in names

        map = ObjectReader.get_properties(obj)
        # assert 2 == len(map)
        assert "ABC" == map["public_field"]
        assert None != map["public_prop"]

    def test_get_map_properties(self):
        map = AnyValueMap.from_tuples(
            "key1", 123,
            "key2", "ABC"
        )

        names = ObjectReader.get_property_names(map)
        assert 2 == len(names)
        assert "key1" in names
        assert "key2" in names

        values = ObjectReader.get_properties(map)
        assert 2 == len(values)
        assert 123 == values["key1"]
        assert "ABC" == values["key2"]

    def test_get_array_properties(self):
        array = AnyValueArray.from_values(123, "ABC")

        names = ObjectReader.get_property_names(array)
        assert 2 == len(names)
        assert "0" in names
        assert "1" in names

        values = ObjectReader.get_properties(array)
        assert 2 == len(values)
        assert 123 == values["0"]
        assert "ABC" == values["1"]

        array = [123, "ABC"]

        names = ObjectReader.get_property_names(array)
        assert 2 == len(names)
        assert "0" in names
        assert "1" in names

        values = ObjectReader.get_properties(array)
        assert 2 == len(values)
        assert 123 == values["0"]
        assert "ABC" == values["1"]
