# -*- coding: utf-8 -*-
from pip_services4_components.config import ConfigParams

from test.containers.DummyAzureFuntionFixture import DummyAzureFunctionFixture
from test.containers.DummyCommandableAzureFunction import DummyCommandableAzureFunction


class TestDummyCommandableAzureFunction:
    _function: DummyCommandableAzureFunction
    fixture: DummyAzureFunctionFixture

    def setup_method(self):
        config = ConfigParams.from_tuples(
            'logger.descriptor', 'pip-services:logger:console:default:1.0',
            'service.descriptor', 'pip-services-dummies:service:default:default:1.0'
        )

        self._function = DummyCommandableAzureFunction()
        self._function.configure(config)
        self._function.open(None)

        self.fixture = DummyAzureFunctionFixture(self._function)

    def teardown_method(self):
        self._function.close(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()
