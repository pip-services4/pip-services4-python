# -*- coding: utf-8 -*-
"""
    tests.validate.test_PropertiesComparisonRule
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.validate import Schema, PropertiesComparisonRule
from .ObjectTest import ObjectTest


class TestPropertiesComparisonRule:

    def test_properties_comparison(self):
        obj = ObjectTest()
        schema = Schema().with_rule(PropertiesComparisonRule("String_Property", "EQ", "Null_Property"))

        obj.string_property = "ABC"
        obj.null_property = "ABC"
        results = schema.validate(obj)
        assert 0 == len(results)

        obj.null_property = "XYZ"
        results = schema.validate(obj)
        assert 1 == len(results)
