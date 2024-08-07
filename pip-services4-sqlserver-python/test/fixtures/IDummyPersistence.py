# -*- coding: utf-8 -*-
from abc import ABC
from typing import List, Union, Optional

from pip_services4_commons.data import  AnyValueMap
from pip_services4_components.context import IContext
from pip_services4_data.query import FilterParams, PagingParams
from pip_services4_persistence.read import IGetter
from pip_services4_persistence.write import IWriter, IPartialUpdater

from test.fixtures import Dummy


class IDummyPersistence(IGetter, IWriter, IPartialUpdater, ABC):

    def get_page_by_filter(self, context: Optional[IContext], filter: Optional[FilterParams],
                           paging: Optional[PagingParams]):
        raise NotImplemented()

    def get_count_by_filter(self, context: Optional[IContext], filter: Optional[FilterParams]):
        raise NotImplemented()

    def get_list_by_ids(self, context: Optional[IContext], ids: List[str]):
        raise NotImplemented()

    def get_one_by_id(self, context: Optional[IContext], ids: List[str]):
        raise NotImplemented()

    def create(self, context: Optional[IContext], item: Dummy):
        raise NotImplemented()

    def update(self, context: Optional[IContext], item: Dummy):
        raise NotImplemented()

    def set(self, context: Optional[IContext], item: Dummy):
        raise NotImplemented()

    def update_partially(self, context: Optional[IContext], id: str, data: AnyValueMap):
        raise NotImplemented()

    def delete_by_id(self, correlation_id: Optional[IContext], id: str):
        raise NotImplemented()

    def delete_by_ids(self, correlation_id: Optional[IContext], ids: List[str]):
        raise NotImplemented()
