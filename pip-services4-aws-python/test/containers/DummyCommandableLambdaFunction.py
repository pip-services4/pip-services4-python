# -*- coding: utf-8 -*-
from pip_services4_components.refer import Descriptor

from pip_services4_aws.containers.CommandableLambdaFunction import CommandableLambdaFunction
from test.DummyFactory import DummyFactory


class DummyCommandableLambdaFunction(CommandableLambdaFunction):
    def __init__(self):
        super().__init__("dummy", "Dummy lambda function")
        self._dependency_resolver.put('service',
                                      Descriptor('pip-services-dummies', 'service', 'default', '*', '*'))
        self._factories.add(DummyFactory())
