# -*- coding: utf-8 -*-
from pip_services4_components.build import Factory
from pip_services4_components.refer import Descriptor

from .DummyService import DummyService

from .controller.DummyCloudFunctionController import DummyCloudFunctionController
from .controller.DummyCommandableCloudFunctionController import DummyCommandableCloudFunctionController


class DummyFactory(Factory):
    DescriptorDummy = Descriptor("pip-services", "factory", "default", "default", "1.0")
    ControllerDescriptor = Descriptor("pip-services", "service", "default", "*", "1.0")
    CloudFunctionServiceDescriptor = Descriptor("pip-services", "controller", "cloudfunc", "*", "1.0")
    CmdCloudFunctionServiceDescriptor = Descriptor("pip-services", "controller", "commandable-cloudfunc", "*",
                                                   "1.0")

    def __init__(self):
        super().__init__()
        self.register_as_type(DummyFactory.ControllerDescriptor, DummyService)
        self.register_as_type(DummyFactory.CloudFunctionServiceDescriptor, DummyCloudFunctionController)
        self.register_as_type(DummyFactory.CmdCloudFunctionServiceDescriptor, DummyCommandableCloudFunctionController)
