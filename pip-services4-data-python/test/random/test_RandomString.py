# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomString
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.random import RandomString

symbols = "_,.:-/.[].{},#-!,$=%.+^.&*-() "
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "01234956789"


class TestRandomString:

    def test_pick(self):
        assert RandomString.pick_char("") == ''

        char_variable = RandomString.pick_char(chars)
        assert chars.find(char_variable) >= 0

        assert '' == RandomString.pick([])

        values = ["ab", "cd"]
        result = RandomString.pick(values)
        assert result in ["ab", "cd"]

    def test_distort(self):
        value = RandomString.distort("abc")
        assert len(value) == 3 or len(value) == 4
        assert value[0:3] in ["Abc", "abc"]

        if len(value) == 4:
            assert symbols.find(value[3]) >= 0

    def test_next_alpha_char(self):
        assert chars.find(RandomString.next_alpha_char()) >= 0

    def test_next_string(self):
        value = RandomString.next_string(3, 5)
        assert 5 >= len(value) >= 3
