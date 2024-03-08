# -*- coding: utf-8 -*-
"""
    tests.convert.test_MapConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.convert import MapConverter
from .StubClass import StubClass


class TestMapConverter:

    def test_to_nullable_map(self):
        assert MapConverter.to_nullable_map(None) is None
        assert MapConverter.to_nullable_map(5) is None

        array = [1, 2]
        map = MapConverter.to_nullable_map(array)
        assert map is not None
        assert 1 == map['0']
        assert 2 == map['1']

        dct = {'field1': 'abc', 'field2': 123}
        map = MapConverter.to_nullable_map(dct)
        assert map is not None
        assert 'abc' == map['field1']
        assert 123 == map['field2']

        assert MapConverter.to_nullable_map('xyz') is None

    def test_object_to_map(self):
        # Handling nulls
        value = None
        result = MapConverter.to_nullable_map(value)
        assert result is None

        # Handling simple objects
        value = StubClass(123, 234)
        result = MapConverter.to_nullable_map(value)
        assert 123 == result["value1"]
        assert 234 == result["value2"]

        # Handling dictionaries
        # args = {}
        # result = MapConverter.to_nullable_map(args)
        # assert args == result

        # Non-recursive conversion
        # args = StubClass(123, StubClass(111, 222))
        # result = MapConverter.to_map(args, None, False)
        # assert result is not None
        # assert 123 == result["value1"]
        # assert result["value2"] is not None
        # assert not isinstance(result["value2"], dict)
        # assert instanceof(result["value2"], StubClass)

        # Recursive conversion
        value = StubClass(123, StubClass(111, 222))
        result = MapConverter.to_nullable_map(value)
        assert isinstance(result, dict)
        assert result is not None
        assert 123 == result["value1"]
        assert result["value2"] is not None
        # assert isinstance(result["value2"], dict)

        # Handling arrays
        value = StubClass([StubClass(111, 222)], None)
        result = MapConverter.to_nullable_map(value)
        assert result is not None
        assert type(result["value1"]) == list
        resultElements = result["value1"]
        resultElement0 = resultElements[0]
        assert resultElement0 is not None
        # assert 111 == resultElement0["value1"]
        # assert 222 == resultElement0["value2"]
