# -*- coding: utf-8 -*-
"""
    test.DummyFactory
    ~~~~~~~~~~~~~~~~~
    
    Dummy factory implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_components.build import Factory
from pip_services4_components.refer import Descriptor

from DummyController import DummyController


class DummyFactory(Factory):
    ControllerDescriptor = Descriptor("pip-services-dummies", "controller", "default", "*", "1.0")

    def __init__(self):
        super().__init__()
        self.register_as_type(DummyFactory.ControllerDescriptor, DummyController)
