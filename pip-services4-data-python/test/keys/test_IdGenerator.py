# -*- coding: utf-8 -*-
"""
    tests.config.test_IdGenerator
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.keys import IdGenerator


class TestIdGenerator:

    def test_next_short(self):
        id1 = IdGenerator.next_short()
        assert id1 != None
        assert len(id1) >= 9

        id2 = IdGenerator.next_short()
        assert id2 != None
        assert len(id2) >= 9
        assert id1 != id2

    def test_next_long(self):
        id1 = IdGenerator.next_long()
        assert id1 != None
        assert len(id1) == 32

        id2 = IdGenerator.next_long()
        assert id2 != None
        assert len(id2) == 32
        assert id1 != id2
