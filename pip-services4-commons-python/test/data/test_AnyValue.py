# -*- coding: utf-8 -*-
"""
    tests.config.test_AnyValue
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.convert import TypeCode

from pip_services4_commons.data import AnyValue


class TestAnyValue:

    def test_get_and_set_any_value(self):
        value = AnyValue()
        assert None == value.get_as_object()

        value.set_as_object(1)
        assert 1 == value.get_as_integer()
        assert 0.001 > 1.0 - value.get_as_float()
        assert "1" == value.get_as_string()

    def test_equal_any_value(self):
        value = AnyValue(1)

        assert 1 == value
        assert 1.0 == value
        assert "1" == value
        assert value.equals_as_type(TypeCode.Float, "1")
