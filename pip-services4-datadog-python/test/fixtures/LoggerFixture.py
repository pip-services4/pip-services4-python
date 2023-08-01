# -*- coding: utf-8 -*-
from pip_services4_components.context import Context
from pip_services4_observability.log import CachedLogger, LogLevel


class LoggerFixture:
    _logger: CachedLogger

    def __init__(self, logger: CachedLogger):
        self._logger = logger

    def test_log_level(self):
        assert self._logger.get_level() >= LogLevel.Nothing
        assert self._logger.get_level() <= LogLevel.Trace

    def test_simple_logging(self):
        self._logger.set_level(LogLevel.Trace)
        ctx = Context.from_trace_id("987")

        self._logger.fatal(ctx, None, "Fatal error message")
        self._logger.error(ctx, None, "Error message")
        self._logger.warn(ctx, "Warning message")
        self._logger.info(ctx, "Information message")
        self._logger.debug(ctx, "Debug message")
        self._logger.trace(ctx, "Trace message")

        self._logger.dump()

        # time.sleep(1)

    def test_error_logging(self):
        try:
            # Raise an exception
            raise Exception('Test error exception')
        except Exception as err:
            ctx = Context.from_trace_id("123")
            self._logger.fatal(ctx, err, "Fatal error")
            self._logger.error(ctx, err, "Recoverable error")

        self._logger.dump()

        # time.sleep(1)
