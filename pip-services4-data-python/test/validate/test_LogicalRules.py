# -*- coding: utf-8 -*-
"""
    tests.validate.test_LogicalRules
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.validate import Schema, OrRule, ValueComparisonRule, AndRule


class TesLogicalRules:

    def test_or_rule(self):
        schema = Schema().with_rule(
            OrRule(
                ValueComparisonRule("=", 1),
                ValueComparisonRule("=", 2)
            )
        )
        result = schema.validate(-100)
        assert 2 == len(result)

        result = schema.validate(1)
        assert 0 == len(result)

        result = schema.validate(200)
        assert 2 == len(result)

    def test_and_rule(self):
        schema = Schema().with_rule(
            AndRule(
                ValueComparisonRule(">", 0),
                ValueComparisonRule("<", 200)
            )
        )
        result = schema.validate(-100)
        assert 1 == len(result)

        result = schema.validate(100)
        assert 0 == len(result)

        result = schema.validate(200)
        assert 1 == len(result)
