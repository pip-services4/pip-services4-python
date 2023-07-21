# -*- coding: utf-8 -*-
"""
    tests.data.test_AnyValueMap
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_commons.data import AnyValueMap


class TestAnyValueMap():
    def test_get_as_string(self):
        message = AnyValueMap.from_tuples("key1", 123,
                                          "key2", "ABC")

        assert len(message) == 2
        assert message.get_as_integer("key1") == 123
        assert message.get_as_string("key2") == "ABC"
