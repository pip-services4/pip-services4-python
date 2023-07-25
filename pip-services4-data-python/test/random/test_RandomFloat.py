# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomFloat
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.random import RandomFloat


class TestRandomFloat:

    def test_next_float(self):
        value = RandomFloat.next_float(5)
        assert value < 5

        value = RandomFloat.next_float(2, 5)
        assert 5 > value > 2

    def test_update_float(self):
        value = RandomFloat.update_float(0, 5)

        assert 5 >= value >= -5
