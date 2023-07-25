# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomBoolean
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.random import RandomBoolean


class TestRandomBoolean:

    def test_chance(self):
        value = RandomBoolean.chance(5, 10)
        assert value or not value

        value = RandomBoolean.chance(5, 5)
        assert value or not value

        value = RandomBoolean.chance(0, 0)
        assert False == value

        value = RandomBoolean.chance(-1, 0)
        assert False == value

        value = RandomBoolean.chance(-1, -1)
        assert False == value
