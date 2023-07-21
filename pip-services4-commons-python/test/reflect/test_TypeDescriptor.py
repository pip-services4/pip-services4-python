# -*- coding: utf-8 -*-
"""
    tests.refer.test_TypeDescriptor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.errors import ConfigException
from pip_services4_commons.reflect import TypeDescriptor


class TestTypeDescriptor:

    def test_from_string(self):
        descriptor = TypeDescriptor.from_string(None)
        assert None == descriptor

        descriptor = TypeDescriptor.from_string("xxx,yyy")
        assert "xxx" == descriptor.get_name()
        assert "yyy" == descriptor.get_library()

        descriptor = TypeDescriptor.from_string("xxx")
        assert "xxx" == descriptor.get_name()
        assert None == descriptor.get_library()

        try:
            descriptor = TypeDescriptor.from_string("xxx,yyy,zzz")
            raise Exception("Wrong descriptor shall raise an error")
        except ConfigException:
            # Ok...
            pass
