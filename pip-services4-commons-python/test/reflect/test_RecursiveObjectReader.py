# -*- coding: utf-8 -*-
"""
    tests.refer.test_RecursiveObjectReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.convert import JsonConverter
from pip_services4_commons.reflect import RecursiveObjectReader


class TestRecursiveObjectReader:

    def test_has_property(self):
        obj = JsonConverter.to_map(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 }, \"value3\": [ 444, "
            "{ \"value311\": 555 } ] } "
        )

        has = RecursiveObjectReader.has_property(obj, "")
        assert False == has

        has = RecursiveObjectReader.has_property(obj, "value1")
        assert True == has

        has = RecursiveObjectReader.has_property(obj, "value2")
        assert True == has

        has = RecursiveObjectReader.has_property(obj, "value2.value21")
        assert True == has

        has = RecursiveObjectReader.has_property(obj, "value2.value31")
        assert False == has

        has = RecursiveObjectReader.has_property(obj, "value2.value21.value211")
        assert False == has

        has = RecursiveObjectReader.has_property(obj, "valueA.valueB.valueC")
        assert False == has

        has = RecursiveObjectReader.has_property(obj, "value3")
        assert True == has

        has = RecursiveObjectReader.has_property(obj, "value3.0")
        assert True == has

        has = RecursiveObjectReader.has_property(obj, "value3.0.value311")
        assert False == has

        has = RecursiveObjectReader.has_property(obj, "value3.1")
        assert True == has

        has = RecursiveObjectReader.has_property(obj, "value3.1.value311")
        assert True == has

        has = RecursiveObjectReader.has_property(obj, "value3.2")
        assert False == has

    def test_get_property(self):
        obj = JsonConverter.to_map(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 }, \"value3\": [ 444, "
            "{ \"value311\": 555 } ] } "
        )

        value = RecursiveObjectReader.get_property(obj, "")
        assert None == value

        value = RecursiveObjectReader.get_property(obj, "value1")
        assert 123 == value

        value = RecursiveObjectReader.get_property(obj, "value2")
        assert None != value

        value = RecursiveObjectReader.get_property(obj, "value2.value21")
        assert 111 == value

        value = RecursiveObjectReader.get_property(obj, "value2.value31")
        assert None == value

        value = RecursiveObjectReader.get_property(obj, "value2.value21.value211")
        assert None == value

        value = RecursiveObjectReader.get_property(obj, "valueA.valueB.valueC")
        assert None == value

        value = RecursiveObjectReader.get_property(obj, "value3")
        assert None != value

        value = RecursiveObjectReader.get_property(obj, "value3.0")
        assert 444 == value

        value = RecursiveObjectReader.get_property(obj, "value3.0.value311")
        assert None == value

        value = RecursiveObjectReader.get_property(obj, "value3.1")
        assert None != value

        value = RecursiveObjectReader.get_property(obj, "value3.1.value311")
        assert 555 == value

        value = RecursiveObjectReader.get_property(obj, "value3.2")
        assert None == value

    def test_get_property_names(self):
        obj = JsonConverter.to_map(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 }, \"value3\": [ 444, "
            "{ \"value311\": 555 } ] } "
        )

        names = RecursiveObjectReader.get_property_names(obj)
        assert 5 == len(names)
        assert "value1" in names
        assert "value2.value21" in names
        assert "value2.value22" in names
        assert "value3.0" in names
        assert "value3.1.value311" in names

    def test_get_properties(self):
        obj = JsonConverter.to_map(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 }, \"value3\": [ 444, "
            "{ \"value311\": 555 } ] } "
        )

        values = RecursiveObjectReader.get_properties(obj)
        assert 5 == len(values)
        assert 123 == values["value1"]
        assert 111 == values["value2.value21"]
        assert 222 == values["value2.value22"]
        assert 444 == values["value3.0"]
        assert 555 == values["value3.1.value311"]
