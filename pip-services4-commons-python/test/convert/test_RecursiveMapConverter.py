# -*- coding: utf-8 -*-
"""
    tests.convert.test_RecursiveMapConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.convert import RecursiveMapConverter


class InitTestClass(object):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


class TestRecursiveMapConverter:

    def test_object_to_map(self):
        # Handling nulls
        value = None
        result = RecursiveMapConverter.to_nullable_map(value)
        assert result == None

        # Handling simple objects
        value = InitTestClass(123, 234)
        result = RecursiveMapConverter.to_nullable_map(value)
        assert 123 == result["value1"]
        assert 234 == result["value2"]

        # Handling dictionaries
        value = {}
        result = RecursiveMapConverter.to_nullable_map(value)
        assert value == result

        # Recursive conversion
        value = InitTestClass(123, InitTestClass(111, 222))
        result = RecursiveMapConverter.to_nullable_map(value)
        assert isinstance(result, dict)
        assert result != None
        assert 123 == result["value1"]
        assert result["value2"] != None
        assert isinstance(result["value2"], dict)

        # Handling arrays
        value = InitTestClass([InitTestClass(111, 222)], None)
        result = RecursiveMapConverter.to_nullable_map(value)
        assert result != None
        assert type(result["value1"]) != list
        resultElements = result["value1"]
        resultElement0 = resultElements[0]
        assert resultElement0 != None
        assert 111 == resultElement0["value1"]
        assert 222 == resultElement0["value2"]

        # Handling map_to_map
        value = {'list': [InitTestClass(111, 222), 10], 'anotherEl': 'test'}
        result = RecursiveMapConverter.to_nullable_map(value)
        assert result != None
        assert type(result) is dict
        assert type(result["list"]) is dict
        value["anotherEl"] = result["anotherEl"]
        assert 111 == result["list"][0]["value1"]
        assert 222 == result["list"][0]["value2"]
