# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomDateTime
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from datetime import datetime

from pip_services4_data.random import RandomDateTime


class TestRandomDateTime:

    def test_next_date(self):
        date = RandomDateTime.next_date(datetime(2015, 2, 1), datetime(2016, 2, 1))
        assert date.year == 2015 or date.year == 2016

        date = RandomDateTime.next_date(datetime.now())
        assert datetime.now().year - 10 <= date.year <= datetime.now().year

    def test_update_datetime(self):
        old_date = datetime(2016, 11, 10, 0, 0, 0, 0)

        date = RandomDateTime.update_datetime(old_date)
        assert (date.timestamp() * 1000) >= (old_date.timestamp() * 1000) - 10 * 24 * 3600000 or (
                date.timestamp() * 1000) >= (old_date.timestamp() * 1000) + 10 * 24 * 3600000

        date = RandomDateTime.update_datetime(old_date, 3 * 24 * 3600000)
        assert (date.timestamp() * 1000) >= (old_date.timestamp() * 1000) - 3 * 24 * 3600000 or (
                date.timestamp() * 1000) >= (old_date.timestamp() * 1000) + 3 * 24 * 3600000

        date = RandomDateTime.update_datetime(old_date, -3)
        assert (date.timestamp() * 1000) == (old_date.timestamp() * 1000)
