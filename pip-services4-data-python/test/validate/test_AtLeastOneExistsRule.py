# -*- coding: utf-8 -*-
"""
    tests.validate.test_AtLeastOneExistRule
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.validate import AtLeastOneExistsRule, Schema
from .ObjectTest import ObjectTest


class TestAtLeastOneExistsRule:

    def test_only_one_exist_rule(self):
        obj = ObjectTest()
        schema = Schema().with_rule(AtLeastOneExistsRule("Missing_Property", "String_Property", "Null_Property"))
        results = schema.validate(obj)
        assert 0 == len(results)

        schema = Schema().with_rule(AtLeastOneExistsRule("String_Property", "Null_Property", "int_Field"))
        results = schema.validate(obj)
        assert 0 == len(results)

        schema = Schema().with_rule(AtLeastOneExistsRule("Missing_Property", "Null_Property"))
        results = schema.validate(obj)
        assert 1 == len(results)
