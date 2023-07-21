# -*- coding: utf-8 -*-
"""
    tests.convert.test_LongConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from datetime import datetime, timezone

from pip_services4_commons.convert import LongConverter


class TestLongConverter:

    def test_to_long(self):
        assert 123 == LongConverter.to_long(123)
        assert 123 == LongConverter.to_long(123.456)
        assert 123 == LongConverter.to_long("123")
        assert 123 == LongConverter.to_long("123.465")
        assert 123 == LongConverter.to_long(datetime.fromtimestamp(123/1000, tz=timezone.utc))

        assert 123 == LongConverter.to_long_with_default(None, 123)
        assert 0 == LongConverter.to_long_with_default(False, 123)
        assert 123 == LongConverter.to_long_with_default("ABC", 123)
