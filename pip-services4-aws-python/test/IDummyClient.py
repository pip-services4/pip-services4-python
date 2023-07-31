# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Optional

from pip_services4_components.context import IContext

from pip_services4_data.query import FilterParams, PagingParams, DataPage

from test.Dummy import Dummy


class IDummyClient(ABC):
    @abstractmethod
    def get_dummies(self, context: Optional[IContext], filter_params: FilterParams, paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_dummy_by_id(self, context: Optional[IContext], dummy_id: str) -> Dummy:
        pass

    @abstractmethod
    def create_dummy(self, context: Optional[IContext], dummy: Dummy) -> Dummy:
        pass

    @abstractmethod
    def update_dummy(self, context: Optional[IContext], dummy: Dummy) -> Dummy:
        pass

    @abstractmethod
    def delete_dummy(self, context: Optional[IContext], dummy_id: str) -> Dummy:
        pass
