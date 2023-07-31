# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import Optional

from pip_services4_data.query import PagingParams, DataPage, FilterParams
from pip_services4_components.context import IContext

from test.Dummy import Dummy


class IDummyService(ABC):
    @abstractmethod
    def get_page_by_filter(self, context: Optional[str], filter_params: FilterParams,
                           paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_one_by_id(self, context: Optional[IContext], id: str) -> Dummy:
        pass

    @abstractmethod
    def create(self, context: Optional[IContext], entity: Dummy) -> Dummy:
        pass

    @abstractmethod
    def update(self, context: Optional[IContext], new_entity: Dummy) -> Dummy:
        pass

    @abstractmethod
    def delete_by_id(self, context: Optional[IContext], id: str) -> Dummy:
        pass
