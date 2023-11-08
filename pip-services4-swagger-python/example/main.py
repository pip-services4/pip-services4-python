# -*- coding: utf-8 -*-

import sys
import os

from pip_services4_components.config import ConfigParams
from pip_services4_components.refer import References, Descriptor, Referencer
from pip_services4_components.run import Opener, Closer
from pip_services4_http.controller import HttpEndpoint, StatusRestController, HeartbeatRestController
from pip_services4_observability.count import LogCounters
from pip_services4_observability.log import ConsoleLogger

from logic.DummyService import DummyService
from controllers.DummyCommandableHttpController import DummyCommandableHttpController
from controllers.DummyRestController import DummyRestController
from pip_services4_swagger.controllers.SwaggerController import SwaggerController

if __name__ == "__main__":
    # add parent directory to path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    # Create components
    logger = ConsoleLogger()
    service = DummyService()
    http_endpoint = HttpEndpoint()
    rest_controller = DummyRestController()
    http_controller = DummyCommandableHttpController()
    status_controller = StatusRestController()
    heartbeat_controller = HeartbeatRestController()
    swagger_controller = SwaggerController()

    components = [
        service,
        http_endpoint,
        rest_controller,
        http_controller,
        status_controller,
        heartbeat_controller,
        swagger_controller
    ]

    try:
        # Configure components
        logger.configure(ConfigParams.from_tuples('level', 'trace'))
        http_endpoint.configure(ConfigParams.from_tuples(
            'connection.protocol', 'http',
            'connection.host', 'localhost',
            'connection.port', 8080
        ))
        rest_controller.configure(ConfigParams.from_tuples('swagger.enable', True))
        http_controller.configure(ConfigParams.from_tuples(
            'base_route', 'dummies2',
            'swagger.enable', True
        ))

        # Set references
        references = References.from_tuples(
            Descriptor('pip-services', 'logger', 'console', 'default', '1.0'), logger,
            Descriptor('pip-services', 'counters', 'log', 'default', '1.0'), LogCounters(),
            Descriptor('pip-services', 'endpoint', 'http', 'default', '1.0'), http_endpoint,
            Descriptor('pip-services', 'service', 'default', 'default', '1.0'), service,
            Descriptor('pip-services', 'controller', 'rest', 'default', '1.0'), rest_controller,
            Descriptor('pip-services', 'controller', 'commandable-http', 'default', '1.0'), http_controller,
            Descriptor('pip-services', 'status-controller', 'rest', 'default', '1.0'), status_controller,
            Descriptor('pip-services', 'heartbeat-controller', 'rest', 'default', '1.0'), heartbeat_controller,
            Descriptor('pip-services', 'swagger-controller', 'http', 'default', '1.0'), swagger_controller
        )

        Referencer.set_references(references, components)

        # Open components
        Opener.open(None, components)

    except Exception as ex:
        logger.error(None, ex, 'Failed to execute the microservice')
        sys.exit(1)


    def terminate():
        Closer.close(None, components)
        sys.exit(0)


    # Wait until user presses ENTER or ctrl+c
    try:
        while True:
            input()
    except KeyboardInterrupt:
        terminate()
        print("Service stopped")
        # Handle any cleanup here if necessary

