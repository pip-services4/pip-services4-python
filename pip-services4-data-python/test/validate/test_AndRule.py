# -*- coding: utf-8 -*-

from pip_services4_data.validate import Schema, AtLeastOneExistsRule, AndRule
from validate.ObjectTest import ObjectTest


class TestAndRule:

    def test_and_rule(self):
        obj = ObjectTest()

        schema = Schema().with_rule(AndRule(AtLeastOneExistsRule("missing_property", "string_property", "null_property"),
                                            AtLeastOneExistsRule("string_property", "null_property", "int_field")))

        results = schema.validate(obj)
        assert len(results) == 0

        schema = Schema().with_rule(AndRule(AtLeastOneExistsRule("missing_property", "string_property", "null_property"),
                                            AtLeastOneExistsRule("missing_property", "null_property")))
        results = schema.validate(obj)
        assert len(results) == 1
