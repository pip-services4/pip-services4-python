# -*- coding: utf-8 -*-
"""
    tests.refer.test_MethodReflector
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.reflect import MethodReflector

from .StubClass import StubClass


class TestMethodReflector:

    def test_has_method(self):
        obj = StubClass()
        has = MethodReflector.has_method(obj, "public_method")
        assert True == has

        has = MethodReflector.has_method(obj, "_private_method")
        assert False == has

        has = MethodReflector.has_method(obj, "unknown_method")
        assert False == has

    def test_invoke_method(self):
        obj = StubClass()
        value = MethodReflector.invoke_method(obj, "public_method", 123, 321)
        assert 444 == value

    def test_get_method_names(self):
        obj = StubClass()
        methods = MethodReflector.get_method_names(obj)
        assert 3 == len(methods)
