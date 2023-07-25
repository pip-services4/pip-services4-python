# -*- coding: utf-8 -*-
"""
    tests.validate.SubObjectTest
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""


class SubObjectTest:

    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    float_field = 432.

    @property
    def null_property(self):
        return self._null_property

    @null_property.setter
    def null_property(self, value):
        self._null_property = value
