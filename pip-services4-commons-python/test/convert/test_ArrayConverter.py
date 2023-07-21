# -*- coding: utf-8 -*-
"""
    tests.convert.test_ArrayConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.convert import ArrayConverter


class TestArrayConverter:

    def test_to_array(self):
        value = ArrayConverter.list_to_array(None)
        assert type(value) == list
        assert len(value) == 0

        value = ArrayConverter.list_to_array(123)
        assert type(value) == list
        assert len(value) == 1
        assert 123 == value[0]

        value = ArrayConverter.list_to_array([123])
        assert type(value) == list
        assert len(value) == 1
        assert 123 == value[0]

        value = ArrayConverter.list_to_array('123')
        assert type(value) == list
        assert len(value) == 1
        assert '123' == value[0]

        value = ArrayConverter.list_to_array(u'123,456')
        assert type(value) == list
        assert len(value) == 2
        assert '123' == value[0]
        assert '456' == value[1]
