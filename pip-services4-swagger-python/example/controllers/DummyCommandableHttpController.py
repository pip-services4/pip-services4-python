# -*- coding: utf-8 -*-
from pip_services4_components.refer import Descriptor
from pip_services4_http.controller import CommandableHttpController


class DummyCommandableHttpController(CommandableHttpController):
    def __init__(self):
        super(DummyCommandableHttpController, self).__init__('dummies2')
        self._dependency_resolver.put('service',
                                      Descriptor('pip-services', 'service', 'default', '*', '*'))

    def register(self):
        # if not (self._swagger_auto and self._swagger_enabled):
        #     self._register_open_api_spec('swagger yaml content')

        super().register()
