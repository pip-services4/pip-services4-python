# -*- coding: utf-8 -*-
from pip_services4_components.config import ConfigParams

from test.controllers.DummyAzureFunction import DummyAzureFunction
from test.controllers.DummyAzureFunctionControllerFixture import DummyAzureFunctionControllerFixture


class TestDummyAzureFunctionController:
    _function_service: DummyAzureFunction
    fixture: DummyAzureFunctionControllerFixture

    def setup_method(self):
        config = ConfigParams.from_tuples(
            'logger.descriptor', 'pip-services:logger:console:default:1.0',
            'service.descriptor', 'pip-services-dummies:service:default:default:1.0',
            'controller.descriptor', 'pip-services-dummies:controller:azurefunc:default:1.0'
        )

        self._function_service = DummyAzureFunction()
        self._function_service.configure(config)
        self._function_service.open(None)

        self.fixture = DummyAzureFunctionControllerFixture(self._function_service)

    def teardown_method(self):
        self.fixture.teardown_method()

    def test_crud_operations(self):
        self.fixture.test_crud_operations()
