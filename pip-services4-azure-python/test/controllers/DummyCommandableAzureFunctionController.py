# -*- coding: utf-8 -*-
from pip_services4_components.refer import Descriptor

from pip_services4_azure.services import CommandableAzureFunctionController


class DummyCommandableAzureFunctionController(CommandableAzureFunctionController):

    def __init__(self):
        super(DummyCommandableAzureFunctionController, self).__init__('dummies')
        self._dependency_resolver.put('service',
                                      Descriptor('pip-services-dummies', 'service', 'default', '*', '*'))
