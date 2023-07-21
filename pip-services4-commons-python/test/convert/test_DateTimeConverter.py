# -*- coding: utf-8 -*-
"""
    tests.convert.test_DateTimeConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from datetime import *

from pip_services4_commons.convert import DateTimeConverter
from pip_services4_commons.convert.UTC import UTC


class TestDateTimeConverter:

    def test_to_datetime(self):
        assert DateTimeConverter.to_datetime(None) is None

        date1 = datetime(1975, 4, 8, 0, 0, 0, 0, UTC)
        assert date1 == DateTimeConverter.to_datetime_with_default(None, date1)
        assert date1 == DateTimeConverter.to_datetime(datetime(1975, 4, 8))

        date2 = DateTimeConverter.to_utc_datetime(datetime.fromtimestamp(123456.))
        assert date2.isoformat() == DateTimeConverter.to_datetime(123456000).isoformat()

        date3 = datetime(1975, 4, 8, 0, 0, 0, 0, UTC)
        assert date3 == DateTimeConverter.to_datetime("1975-04-08T00:00:00Z")

        assert DateTimeConverter.to_datetime("XYZ") is None
