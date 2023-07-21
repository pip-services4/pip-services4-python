# -*- coding: utf-8 -*-
"""
    tests.convert.test_FloatConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.convert import FloatConverter


class TestFloatConverter:

    def test_to_float(self):
        assert abs(123 - FloatConverter.to_float(123)) < 0.001
        assert abs(123.456 - FloatConverter.to_float(123.456)) < 0.001
        assert abs(123.456 - FloatConverter.to_float("123.456")) < 0.001

        assert abs(123 - FloatConverter.to_float_with_default(None, 123)) < 0.001
        assert abs(0 - FloatConverter.to_float_with_default(False, 123)) < 0.001
        assert abs(123 - FloatConverter.to_float_with_default("ABC", 123)) < 0.001
