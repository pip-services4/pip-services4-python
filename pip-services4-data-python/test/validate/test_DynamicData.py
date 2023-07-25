# -*- coding: utf-8 -*-
import json

from pip_services4_commons.convert import TypeCode

from pip_services4_data.validate import ObjectSchema


class TestDynamicData:

    def test_validate_dynamic_data(self):
        dynamic_string = '{ "string_field": "ABC", "date_field": "2019-01-01T11:30:00.00", ' \
                         '"int_field": 123, "float_field": 123.456 }'
        dynamic_object = json.loads(dynamic_string)

        schema = ObjectSchema() \
            .with_required_property("string_field", TypeCode.String) \
            .with_required_property("date_field", TypeCode.DateTime) \
            .with_required_property("int_field", TypeCode.Integer) \
            .with_required_property("float_field", TypeCode.Float)

        results = schema.validate(dynamic_object)
        assert len(results) == 0
