# -*- coding: utf-8 -*-
"""
    tests.convert.test_JsonConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.convert import JsonConverter, DateTimeConverter, TypeCode


class TestJsonConverter:

    def test_to_json(self):
        assert JsonConverter.to_json(None) is None
        assert '123' == JsonConverter.to_json(123)
        assert "\"ABC\"" == JsonConverter.to_json('ABC')

        filter = {"Key1": 123, "Key2": "ABC"}
        json_filter = JsonConverter.to_json(filter)
        assert '{"Key1": 123, "Key2": "ABC"}' == json_filter

        array = [123, "ABC"]
        json_array = JsonConverter.to_json(array)
        assert '[123, "ABC"]' == json_array

        date = DateTimeConverter.to_datetime("1975-04-08T00:00:00.000Z")
        json_date = JsonConverter.to_json(date)
        assert "\"1975-04-08T00:00:00.000Z\"", json_date

    def test_from_json(self):
        assert 123 == JsonConverter.from_json(TypeCode.Integer, '123')
        assert 'ABC' == JsonConverter.from_json(TypeCode.String, '"ABC"')

        filter = JsonConverter.from_json(None, '{"Key2": "ABC", "Key1": "123"}')
        assert isinstance(filter, dict)

        array = JsonConverter.from_json(TypeCode.Array, "[123,\"ABC\"]")
        assert len(array) == 2

        date = DateTimeConverter.to_datetime("1975-04-08T00:00:00.000Z")
        json_date = JsonConverter.from_json(TypeCode.DateTime, "\"1975-04-08T00:00Z\"")
        assert date.timestamp() == json_date.timestamp()

    def test_json_to_map(self):
        # Handling simple objects
        value = '{ "value1":123, "value2":234 }'
        result = JsonConverter.to_nullable_map(value)
        assert 123 == result["value1"]
        assert 234 == result["value2"]

        # Recursive conversion
        value = '{ "value1":123, "value2": { "value1": 111, "value2": 222 } }'
        result = JsonConverter.to_nullable_map(value)
        assert result != None
        assert 123 == result["value1"]
        assert result["value2"] != None
        assert isinstance(result["value2"], dict)

        # Handling arrays
        value = '{ "value1": [{ "value1": 111, "value2": 222 }] }'
        result = JsonConverter.to_nullable_map(value)
        assert result != None
        assert type(result["value1"]) == list
        resultElements = result["value1"]
        resultElement0 = resultElements[0]
        assert resultElement0 != None
        assert 111 == resultElement0["value1"]
        assert 222 == resultElement0["value2"]
