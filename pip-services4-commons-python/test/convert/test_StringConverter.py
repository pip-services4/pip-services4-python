# -*- coding: utf-8 -*-
"""
    tests.convert.test_StringConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from datetime import datetime

from pip_services4_commons.convert import StringConverter


class TestStringConverter:

    def test_to_string(self):
        assert StringConverter.to_nullable_string(None) == None
        assert "xyz" == StringConverter.to_string("xyz")
        assert "123" == StringConverter.to_string(123)
        assert "True" == StringConverter.to_string(True)
        assert "1975-04-08T19:00:00Z" == StringConverter.to_string(datetime(1975, 4, 8, 19, 0, 0, 0))

        assert "xyz" == StringConverter.to_string_with_default(None, "xyz")
