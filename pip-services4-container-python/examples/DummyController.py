# -*- coding: utf-8 -*-
"""
    test.DummyController
    ~~~~~~~~~~~~~~~~~~~~
    
    Dummy controller implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from typing import Optional

from pip_services4_components.config import IReconfigurable, ConfigParams
from pip_services4_components.context.IContext import IContext
from pip_services4_components.refer import IReferenceable, IReferences
from pip_services4_components.run import IOpenable
from pip_services4_components.exec import INotifiable
from pip_services4_components.exec import FixedRateTimer
from pip_services4_components.exec import Parameters
from pip_services4_observability.log import CompositeLogger


class DummyController(IReferenceable, IReconfigurable, IOpenable, INotifiable):
    __timer: FixedRateTimer = None
    __logger: CompositeLogger = None
    __message: str = None
    __counter: int = None

    def __init__(self):
        self.__message = "Hello World!"
        self.__logger = CompositeLogger()
        self.__timer = FixedRateTimer(self, 1000, 1000)
        self.__counter = 0

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value

    @property
    def counter(self) -> int:
        return self.__counter

    @counter.setter
    def counter(self, value: int):
        self.__counter = value

    def configure(self, config: ConfigParams):
        self.__message = config.get_as_string_with_default("message", self.__message)

    def set_references(self, references: IReferences):
        self.__logger.set_references(references)

    def is_open(self) -> bool:
        return self.__timer.is_started()

    def open(self, context: Optional[IContext]):
        self.__timer.start()
        self.__logger.trace(context, "Dummy controller opened")

    def close(self, context: Optional[IContext]):
        self.__timer.stop()
        self.__logger.trace(context, "Dummy controller closed")

    def notify(self, context: Optional[IContext], args: Parameters):
        self.counter += 1
        self.__logger.info(context, "%d - %s", self.counter, self.message)
