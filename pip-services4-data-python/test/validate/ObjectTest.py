# -*- coding: utf-8 -*-
"""
    tests.validate.ObjectTest
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from .SubObjectTest import SubObjectTest


class ObjectTest:

    def __init__(self):
        self.__private_field = 124
        self.__private_property = "XYZ"
        self.int_field = 12345
        self.string_property = "ABC"
        self.null_property = None
        self.int_array_property = [1, 2, 3]
        self.string_list_property = ["AAA", "BBB"]
        self.map_property = {'Key1': 111, 'Key2': 222}
        self.sub_object_property = SubObjectTest("1")
        self.sub_array_property = [SubObjectTest("2"), SubObjectTest("3")]
