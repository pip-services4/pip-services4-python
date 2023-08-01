# -*- coding: utf-8 -*-
from pip_services4_components.build import Factory
from pip_services4_components.refer import Descriptor

from test.DummyService import DummyService
from test.controllers.DummyAzureFunctionController import DummyAzureFunctionController
from test.controllers.DummyCommandableAzureFunctionController import DummyCommandableAzureFunctionController


class DummyFactory(Factory):
    FactoryDescriptor = Descriptor("pip-services-dummies", "factory", "default", "default", "1.0")
    ServiceDescriptor = Descriptor("pip-services-dummies", "service", "default", "*", "1.0")
    AzureFunctionControllerDescriptor = Descriptor("pip-services-dummies", "controller", "azurefunc", "*", "1.0")
    CmdAzureFunctionControllerDescriptor = Descriptor("pip-services-dummies", "controller", "commandable-azurefunc", "*",
                                                   "1.0")

    def __init__(self):
        super(DummyFactory, self).__init__()
        self.register_as_type(DummyFactory.ServiceDescriptor, DummyService)
        self.register_as_type(DummyFactory.AzureFunctionControllerDescriptor, DummyAzureFunctionController)
        self.register_as_type(DummyFactory.CmdAzureFunctionControllerDescriptor, DummyCommandableAzureFunctionController)
