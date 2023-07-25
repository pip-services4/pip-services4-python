# -*- coding: utf-8 -*-
"""
    tests.validate.test_ValueComparisonRule
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.validate import ValueComparisonRule, Schema


class TestValueComparisonRule:

    def test_equal_comparison(self):
        schema = Schema().with_rule(ValueComparisonRule("EQ", 123))
        results = schema.validate(123)
        assert 0 == len(results)

        results = schema.validate(432)
        assert 1 == len(results)

        schema = Schema().with_rule(ValueComparisonRule("EQ", "ABC"))
        results = schema.validate("ABC")
        assert 0 == len(results)

    def test_not_equal_comparison(self):
        schema = Schema().with_rule(ValueComparisonRule("NE", 123))
        results = schema.validate(123)
        assert 1 == len(results)

        results = schema.validate(432)
        assert 0 == len(results)

        schema = Schema().with_rule(ValueComparisonRule("NE", "ABC"))
        results = schema.validate("XYZ")
        assert 0 == len(results)

    def test_less_comparison(self):
        schema = Schema().with_rule(ValueComparisonRule("LE", 123))
        results = schema.validate(123)
        assert 0 == len(results)

        results = schema.validate(432)
        assert 1 == len(results)

        schema = Schema().with_rule(ValueComparisonRule("LT", 123))
        results = schema.validate(123)
        assert 1 == len(results)

    def test_more_comparison(self):
        schema = Schema().with_rule(ValueComparisonRule("GE", 123))
        results = schema.validate(123)
        assert 0 == len(results)

        results = schema.validate(432)
        assert 0 == len(results)

        schema = Schema().with_rule(ValueComparisonRule("GT", 123))
        results = schema.validate(123)
        assert 1 == len(results)

    def test_match_comparison(self):
        schema = Schema().with_rule(ValueComparisonRule("LIKE", "A.*"))
        results = schema.validate("ABC")
        assert 0 == len(results)

        results = schema.validate("XYZ")
        assert 1 == len(results)
