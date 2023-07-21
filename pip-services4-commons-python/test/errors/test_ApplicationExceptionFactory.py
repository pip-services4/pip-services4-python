# -*- coding: utf-8 -*-
from pip_services4_commons.data import StringValueMap

from pip_services4_commons.errors import ErrorDescription, ErrorCategory, ApplicationExceptionFactory, UnknownException, \
    InternalException, ConfigException, ConnectionException, InvocationException, FileException, BadRequestException, \
    UnauthorizedException, ConflictException, NotFoundException, UnsupportedException


class TestApplicationExceptionFactory:

    descr: ErrorDescription

    def check_properties(self, ex):
        assert ex is not None
        assert self.descr.cause, ex.cause
        assert self.descr.stack_trace, ex.stack_trace
        assert self.descr.details, ex.details
        assert self.descr.category, ex.category

    def setup_method(self):
        self.descr = ErrorDescription()
        self.descr.trace_id = "trace_id"
        self.descr.code = "code"
        self.descr.message = "message"
        self.descr.status = 777
        self.descr.cause = "cause"
        self.descr.stack_trace = "stackTrace"

        map = StringValueMap()
        map.put('key', 'args')

        self.descr.details = map

    def test_create_from_unknown(self):
        self.descr.category = ErrorCategory.Unknown

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, UnknownException) is True

    def test_create_from_internal(self):
        self.descr.category = ErrorCategory.Internal

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, InternalException)

    def test_create_from_misconfiguration(self):
        self.descr.category = ErrorCategory.Misconfiguration

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, ConfigException)

    def test_create_from_no_response(self):
        self.descr.category = ErrorCategory.NoResponse

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, ConnectionException)

    def test_create_from_failed_invocation(self):
        self.descr.category = ErrorCategory.FailedInvocation

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, InvocationException)

    def test_create_from_no_file_access(self):
        self.descr.category = ErrorCategory.FileError

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, FileException)

    def test_create_from_bad_request(self):
        self.descr.category = ErrorCategory.BadRequest

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, BadRequestException)

    def test_create_from_unauthorized(self):
        self.descr.category = ErrorCategory.Unauthorized

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, UnauthorizedException)

    def test_create_from_conflict(self):
        self.descr.category = ErrorCategory.Conflict

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, ConflictException)

    def test_create_from_not_found(self):
        self.descr.category = ErrorCategory.NotFound

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, NotFoundException)

    def test_create_from_unsupported(self):
        self.descr.category = ErrorCategory.Unsupported

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, UnsupportedException)

    def test_create_from_default(self):
        self.descr.category = 'any_other'

        ex = ApplicationExceptionFactory.create(self.descr)

        self.check_properties(ex)

        assert isinstance(ex, UnknownException)



