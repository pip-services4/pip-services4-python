# -*- coding: utf-8 -*-

from abc import ABC
from typing import Optional

from pip_services4_components.context import IContext
from pip_services4_data.query import FilterParams, PagingParams, DataPage

from test.Dummy import Dummy


class IDummyService(ABC):
    def get_page_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        pass

    def get_one_by_id(self, context: Optional[IContext], id: str) -> Dummy:
        pass

    def create(self, context: Optional[IContext], entity: Dummy) -> Dummy:
        pass

    def update(self, context: Optional[IContext], entity: Dummy) -> Dummy:
        pass

    def delete_by_id(self, context: Optional[IContext], id: str) -> Dummy:
        pass
