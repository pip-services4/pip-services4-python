# -*- coding: utf-8 -*-
"""
    tests.refer.test_RecursiveObjectWriter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.convert import JsonConverter
from pip_services4_commons.data import AnyValueMap
from pip_services4_commons.reflect import RecursiveObjectReader
from pip_services4_commons.reflect import RecursiveObjectWriter


class TestRecursiveObjectWriter:

    def test_set_property(self):
        obj = JsonConverter.to_map(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 }, \"value3\": [ 444, "
            "{ \"value311\": 555 } ] } "
        )

        # RecursiveObjectWriter.set_property(obj, "", None)
        RecursiveObjectWriter.set_property(obj, "value1", "AAA")
        RecursiveObjectWriter.set_property(obj, "value2", "BBB")
        RecursiveObjectWriter.set_property(obj, "value3.1.value312", "CCC")
        RecursiveObjectWriter.set_property(obj, "value3.3", "DDD")
        RecursiveObjectWriter.set_property(obj, "value4.1", "EEE")

        values = RecursiveObjectReader.get_properties(obj)
        assert 8 == len(values)
        assert "AAA" == values["value1"]
        assert "BBB" == values["value2"]
        assert 444 == values["value3.0"]
        assert 555 == values["value3.1.value311"]
        assert "CCC" == values["value3.1.value312"]
        assert None == values["value3.2"]
        assert "DDD" == values["value3.3"]
        assert "EEE" == values["value4.1"]

    def test_set_properties(self):
        obj = JsonConverter.to_map(
            "{ \"value1\": 123, \"value2\": { \"value21\": 111, \"value22\": 222 }, \"value3\": [ 444, "
            "{ \"value311\": 555 } ] } "
        )

        values = AnyValueMap.from_tuples(
            "value1", "AAA",
            "value2", "BBB",
            "value3.1.value312", "CCC",
            "value3.3", "DDD",
            "value4.1", "EEE"
        )
        RecursiveObjectWriter.set_properties(obj, values)

        values = RecursiveObjectReader.get_properties(obj)
        assert 8 == len(values)
        assert "AAA" == values["value1"]
        assert "BBB", values["value2"]
        assert 444 == values["value3.0"]
        assert 555 == values["value3.1.value311"]
        assert "CCC", values["value3.1.value312"]
        assert None is values["value3.2"]
        assert "DDD" == values["value3.3"]
        assert "EEE" == values["value4.1"]
