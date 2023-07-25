# -*- coding: utf-8 -*-
"""
    tests.validate.test_Schema
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_commons.convert import TypeCode

from pip_services4_data.validate import ObjectSchema, Schema, ArraySchema, MapSchema
from .ObjectTest import ObjectTest


class TestSchema:

    def test_empty_schema(self):
        schema = ObjectSchema()
        results = schema.validate(None)
        assert 0 == len(results)

    def test_required(self):
        schema = Schema().make_required()
        results = schema.validate(None)
        assert 1 == len(results)

    def test_unexpected(self):
        schema = ObjectSchema()
        obj = ObjectTest()
        results = schema.validate(obj)
        assert 10 == len(results)

    def test_optional_properties(self):
        schema = ObjectSchema() \
            .with_optional_property("int_field", None) \
            .with_optional_property("string_property", None) \
            .with_optional_property("null_property", None) \
            .with_optional_property("int_array_property", None) \
            .with_optional_property("string_list_property", None) \
            .with_optional_property("map_property", None) \
            .with_optional_property("sub_object_property", None) \
            .with_optional_property("sub_array_property", None)

        obj = ObjectTest()
        results = schema.validate(obj)
        assert 2 == len(results)

    def test_required_properties(self):
        schema = ObjectSchema() \
            .with_required_property('__private_field') \
            .with_required_property('__private_property') \
            .with_required_property("int_field") \
            .with_required_property("string_property") \
            .with_required_property("null_property") \
            .with_required_property("int_array_property") \
            .with_required_property("string_list_property") \
            .with_required_property("map_property") \
            .with_required_property("sub_object_property") \
            .with_required_property("sub_array_property")

        obj = ObjectTest()
        obj.sub_array_property = None

        results = schema.validate(obj)
        assert 2 == len(results)

    def test_object_types(self):
        schema = ObjectSchema() \
            .with_required_property('__private_field') \
            .with_required_property('__private_property') \
            .with_required_property("int_field", TypeCode.Long) \
            .with_required_property("string_property", TypeCode.String) \
            .with_optional_property("null_property", TypeCode.Object) \
            .with_required_property("int_array_property", TypeCode.Array) \
            .with_required_property("string_list_property", TypeCode.Array) \
            .with_required_property("map_property", TypeCode.Map) \
            .with_required_property("sub_object_property", TypeCode.Object) \
            .with_required_property("sub_array_property", TypeCode.Array)

        obj = ObjectTest()
        results = schema.validate(obj)
        assert 0 == len(results)

    def test_string_types(self):
        schema = ObjectSchema() \
            .with_required_property('__private_field') \
            .with_required_property('__private_property') \
            .with_required_property("int_field", TypeCode.Long) \
            .with_required_property("string_property", TypeCode.String) \
            .with_optional_property("null_property", TypeCode.Object) \
            .with_required_property("int_array_property", TypeCode.Array) \
            .with_required_property("string_list_property", TypeCode.Array) \
            .with_required_property("map_property", TypeCode.Map) \
            .with_required_property("sub_object_property", TypeCode.Map) \
            .with_required_property("sub_array_property", TypeCode.Array)

        obj = ObjectTest()
        obj.sub_object_property = {'test_map': 123}
        results = schema.validate(obj)
        assert 0 == len(results)

    def test_sub_schema(self):
        sub_schema = ObjectSchema() \
            .with_required_property("id", TypeCode.String) \
            .with_required_property("float_field", TypeCode.Double) \
            .with_optional_property("null_property", TypeCode.Map)

        schema = ObjectSchema() \
            .with_required_property('__private_field') \
            .with_required_property('__private_property') \
            .with_required_property("int_field", TypeCode.Long) \
            .with_required_property("string_property", TypeCode.String) \
            .with_optional_property("null_property", TypeCode.Object) \
            .with_required_property("int_array_property", TypeCode.Array) \
            .with_required_property("string_list_property", TypeCode.Array) \
            .with_required_property("map_property", TypeCode.Map) \
            .with_required_property("sub_object_property", sub_schema) \
            .with_required_property("sub_array_property", TypeCode.Array)

        obj = ObjectTest()
        results = schema.validate(obj)
        assert 0 == len(results)

    def test_array_and_map_schema(self):
        sub_schema = ObjectSchema() \
            .with_required_property("id", TypeCode.String) \
            .with_required_property("float_field", TypeCode.Double) \
            .with_optional_property("null_property", TypeCode.Map)

        schema = ObjectSchema() \
            .with_required_property('__private_field') \
            .with_required_property('__private_property') \
            .with_required_property("int_field", TypeCode.Long) \
            .with_required_property("string_property", TypeCode.String) \
            .with_optional_property("null_property", TypeCode.Object) \
            .with_required_property("int_array_property", ArraySchema(TypeCode.Long)) \
            .with_required_property("string_list_property", ArraySchema(TypeCode.String)) \
            .with_required_property("map_property", MapSchema(TypeCode.String, TypeCode.Long)) \
            .with_required_property("sub_object_property", sub_schema) \
            .with_required_property("sub_array_property", ArraySchema(sub_schema))

        obj = ObjectTest()
        results = schema.validate(obj)
        assert 0 == len(results)
