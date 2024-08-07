# -*- coding: utf-8 -*-
from typing import Callable

import bottle
from pip_services4_commons.errors import UnauthorizedException

from pip_services4_http.controller.HttpResponseSender import HttpResponseSender


class BasicAuthorizer:

    def anybody(self) -> Callable:
        return lambda: None

    def signed(self) -> Callable:
        def inner():
            if bottle.request.user is None:
                return HttpResponseSender.send_error(UnauthorizedException(
                    None,
                    'NOT_SIGNED',
                    'User must be signed in to perform this operation '
                ).with_status(401))

        return inner
