# -*- coding: utf-8 -*-
from pip_services4_components.refer import Descriptor

from pip_services4_aws.controllers.CommandableLambdaController import CommandableLambdaController


class DummyCommandableLambdaController(CommandableLambdaController):
    def __init__(self):
        super().__init__('dummies')
        self._dependency_resolver.put('service',
                                      Descriptor('pip-services-dummies', 'service', 'default', '*', '*'))
