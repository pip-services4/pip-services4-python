# -*- coding: utf-8 -*-

from datetime import datetime, timezone

from pip_services4_commons.convert.DoubleConverter import DoubleConverter


class TestDoubleConverter:

    def test_to_decimal(self):
        assert 123 == DoubleConverter.to_double(123)
        assert 123.456 == DoubleConverter.to_double(123.456)
        assert 123.456 == DoubleConverter.to_double('123.456')
        assert 123 == DoubleConverter.to_double(datetime.fromtimestamp(123 / 1000, tz=timezone.utc))

        assert 123 == DoubleConverter.to_double_with_default(None, 123)
        assert 0 == DoubleConverter.to_double_with_default(False, 123)
        assert 123 == DoubleConverter.to_double_with_default('ABC', 123)
