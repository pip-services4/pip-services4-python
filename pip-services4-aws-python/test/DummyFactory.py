# -*- coding: utf-8 -*-
from pip_services4_components.build import Factory
from pip_services4_components.refer import Descriptor

from test.DummyService import DummyService
from test.controllers.DummyCommandableLambdaController import DummyCommandableLambdaController
from test.controllers.DummyLambdaController import DummyLambdaController


class DummyFactory(Factory):
    DescriptorDummy = Descriptor("pip-services-dummies", "factory", "default", "default", "1.0")
    ControllerDescriptor = Descriptor("pip-services-dummies", "service", "default", "*", "1.0")
    LambdaServiceDescriptor = Descriptor("pip-services-dummies", "controller", "lambda", "*", "1.0")
    CmdLambdaServiceDescriptor = Descriptor("pip-services-dummies", "controller", "commandable-lambda", "*", "1.0")

    def __init__(self):
        super().__init__()
        self.register_as_type(DummyFactory.ControllerDescriptor, DummyService)
        self.register_as_type(DummyFactory.LambdaServiceDescriptor, DummyLambdaController)
        self.register_as_type(DummyFactory.CmdLambdaServiceDescriptor, DummyCommandableLambdaController)
