# -*- coding: utf-8 -*-
"""
    tests.refer.test_ObjectWriter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import datetime

from pip_services4_commons.data import AnyValueArray
from pip_services4_commons.data import AnyValueMap
from pip_services4_commons.reflect import ObjectWriter
from .StubClass import StubClass


class TestObjectWriter:

    def test_set_object_property(self):
        obj = StubClass()

        ObjectWriter.set_property(obj, "private_pield", "XYZ")

        ObjectWriter.set_property(obj, "public_field", "AAAA")
        assert "AAAA" == obj.public_field

        now = datetime.datetime.now()
        ObjectWriter.set_property(obj, "public_prop", now)
        assert now == obj.public_prop

        ObjectWriter.set_property(obj, "public_prop", "BBBB")
        assert "BBBB" == obj.public_prop

    def test_set_map_property(self):
        map = AnyValueMap.from_tuples(
            "key1", 123,
            "key2", "ABC"
        )

        ObjectWriter.set_property(map, "key3", "AAAA")
        assert "AAAA" == map.get("key3")

        ObjectWriter.set_property(map, "Key1", 5555)
        assert 5555 == map.get("key1")

        ObjectWriter.set_property(map, "Key2", "BBBB")
        assert "BBBB" == map.get("key2")

    def test_set_array_property(self):
        array = AnyValueArray.from_values(123, "ABC")

        ObjectWriter.set_property(array, "3", "AAAA")
        assert 4 == len(array)
        assert "AAAA" == array[3]

        ObjectWriter.set_property(array, "0", 1111)
        assert 1111 == array[0]

        ObjectWriter.set_property(array, "1", "BBBB")
        assert "BBBB" == array[1]

        array = [123, "ABC"]

        ObjectWriter.set_property(array, "3", "AAAA")
        assert 4 == len(array)
        assert "AAAA" == array[3]

        ObjectWriter.set_property(array, "0", 1111)
        assert 1111 == array[0]

        ObjectWriter.set_property(array, "1", "BBBB")
        assert "BBBB" == array[1]
