# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomText
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.random import RandomText


class TestRandomText:

    def test_phrase(self):
        assert RandomText.phrase(-1) == ""
        assert RandomText.phrase(-1, -2) == ""
        assert RandomText.phrase(-1, 0) == ""
        assert RandomText.phrase(-2, -1) == ""

        text = RandomText.phrase(4)
        assert 4 <= len(text) <= 10
        text = RandomText.phrase(4, 10)
        assert len(text) >= 4

    def test_name(self):
        text = RandomText.name()
        assert text.find(" ") > 0

    def test_phone(self):
        text = RandomText.phone()
        assert text.find("(") >= 0
        assert text.find(")") > 0
        assert text.find("-") > 0

    def test_email(self):
        text = RandomText.email()
        assert text.find("@") > 0
        assert text.find(".com") > 0
