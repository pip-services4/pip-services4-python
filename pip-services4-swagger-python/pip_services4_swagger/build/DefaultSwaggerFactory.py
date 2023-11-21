# -*- coding: utf-8 -*-

from pip_services4_components.build import Factory
from pip_services4_components.refer import Descriptor

from pip_services4_swagger.controllers.SwaggerController import SwaggerController


class DefaultSwaggerFactory(Factory):
    """
    Creates Swagger components by their descriptors.

    See :class:`Factory <pip_services4_components.build.Factory.Factory>`
    :class:`HttpEndpoint <pip_services4_http.controllers.HttpEndpoint.HttpEndpoint>`
    :class:`HeartbeatRestController <pip_services4_http.controllers.HeartbeatRestController.HeartbeatRestController>`
    :class:`StatusRestController <pip_services4_http.controllers.StatusRestController.StatusRestController>`
    """
    descriptor = Descriptor("pip-services", "factory", "swagger", "default", "1.0")
    swagger_service_descriptor = Descriptor("pip-services", "swagger-controller", "*", "*", "1.0")

    def __init__(self):
        super(DefaultSwaggerFactory, self).__init__()
        self.register_as_type(DefaultSwaggerFactory.swagger_service_descriptor, SwaggerController)
