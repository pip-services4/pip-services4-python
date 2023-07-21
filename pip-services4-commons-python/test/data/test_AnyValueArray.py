# -*- coding: utf-8 -*-
"""
    tests.config.test_AnyValueMap
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.data import AnyValueArray


class TestAnyValueMap:

    def test_create_value_array(self):
        array = AnyValueArray()
        assert 0 == len(array)

        array = AnyValueArray([1, 2, 3])
        assert 3 == len(array)
        assert "1,2,3" == str(array)

        array = AnyValueArray.from_string("Fatal,Error,Info,", ",")
        assert 4 == len(array)

        array = AnyValueArray((1, 2, 3))
        assert 3 == len(array)
        assert 1 in array

        values = [1, 2, 3]
        array = AnyValueArray(values)
        assert 3 == len(array)
        assert 2 in array
