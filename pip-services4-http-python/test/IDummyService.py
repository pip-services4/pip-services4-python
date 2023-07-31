# -*- coding: utf-8 -*-
"""
    test.IDummyController
    ~~~~~~~~~~~~~~~~~~~~~
    
    Interface for dummy controllers
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from typing import Optional

from pip_services4_components.context import IContext
from pip_services4_data.query import FilterParams, PagingParams, DataPage

from test import Dummy


class IDummyService:
    def get_page_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        raise NotImplementedError('Method from interface definition')

    def get_one_by_id(self, context: Optional[IContext], id: str) -> Dummy:
        raise NotImplementedError('Method from interface definition')

    def create(self, context: Optional[IContext], item: Dummy) -> Dummy:
        raise NotImplementedError('Method from interface definition')

    def update(self, context: Optional[IContext], new_item: Dummy) -> Dummy:
        raise NotImplementedError('Method from interface definition')

    def delete_by_id(self, context: Optional[IContext], id: str) -> Dummy:
        raise NotImplementedError('Method from interface definition')

    def check_trace_id(self, context: Optional[IContext]) -> str:
        raise NotImplementedError('Method from interface definition')
