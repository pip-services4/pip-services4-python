# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomInteger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.random import RandomInteger


class TestRandomInteger:

    def test_next_integer(self):
        value = RandomInteger.next_integer(5)
        assert value <= 5

        value = RandomInteger.next_integer(2, 5)
        assert 5 >= value >= 2

    def test_update_integer(self):
        value = RandomInteger.update_integer(0, 5)
        assert 5 >= value >= -5

        value = RandomInteger.update_integer(5, 0)

        value = RandomInteger.update_integer(0)
        assert value == 0

    def test_sequence(self):
        seq = RandomInteger.sequence(1, 5)
        assert 5 >= len(seq) >= 1

        seq = RandomInteger.sequence(-1, 0)
        assert len(seq) == 0

        seq = RandomInteger.sequence(-1, -4)
        assert len(seq) == 0

        seq = RandomInteger.sequence(4, 4)
        assert len(seq) == 4

        seq = RandomInteger.sequence(5)
        assert len(seq) == 5
