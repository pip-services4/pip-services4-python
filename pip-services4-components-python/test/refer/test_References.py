# -*- coding: utf-8 -*-
"""
    tests.refer.test_References
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_components.refer import References


class TestReferences:

    def test_put(self):
        refs = References()
        refs.put(111, "AAA")
        refs.put(222, "BBB")
        refs.put(333, "CCC")
        refs.put(444, "DDD")
        assert 4 == len(refs.get_all())

    def test_get(self):
        refs = References.from_tuples(
            111, "AAA",
            222, "BBB",
            333, "CCC",
            444, "DDD"
        )
        assert 4 == len(refs.get_all())

        item = refs.get_one_optional(555)
        assert item is None

        item = refs.get_one_required(111)
        assert "AAA" == item

        items = refs.get_optional(666)
        assert 0 == len(items)

        items = refs.get_required(333)
        assert 1 == len(items)
