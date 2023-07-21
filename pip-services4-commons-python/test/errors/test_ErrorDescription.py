# -*- coding: utf-8 -*-
"""
    tests.errors.test_ErrorDescription
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_commons.errors import ApplicationExceptionFactory
from pip_services4_commons.errors import ErrorCategory
from pip_services4_commons.errors import ErrorDescriptionFactory
from pip_services4_commons.errors import UnsupportedException


class TestApplicationException:

    def test_from_exception(self):
        error = UnsupportedException('123', 'TEST_ERROR', 'Test error')
        description = ErrorDescriptionFactory.create(error)

        assert ErrorCategory.Unsupported == description.category
        assert '123' == description.trace_id
        assert 'TEST_ERROR' == description.code
        assert 'Test error' == description.message

    def test_create_exception(self):
        error = UnsupportedException('123', 'TEST_ERROR', 'Test error')
        description = ErrorDescriptionFactory.create(error)

        error = ApplicationExceptionFactory.create(description)

        assert isinstance(error, UnsupportedException)
        assert ErrorCategory.Unsupported == error.category
        assert '123' == error.trace_id
        assert 'TEST_ERROR' == error.code
        assert 'Test error' == error.message
