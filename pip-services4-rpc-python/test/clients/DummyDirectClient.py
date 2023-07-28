# -*- coding: utf-8 -*-
"""
    test.rest.DummyDirectClient
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy direct client implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from typing import Optional

from pip_services4_components.refer import Descriptor
from pip_services4_components.context import IContext
from pip_services4_data.query import FilterParams, PagingParams, DataPage

from pip_services4_rpc.clients import DirectClient
from .IDummyClient import IDummyClient
from .. import Dummy


class DummyDirectClient(DirectClient, IDummyClient):

    def __init__(self):
        super(DummyDirectClient, self).__init__()
        self._dependency_resolver.put('controller', Descriptor('pip-services-dummies', 'controller', '*', '*', '*'))

    def get_page_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        timing = self._instrument(context, 'dummy.get_page_by_filter')
        try:
            return self._controller.get_page_by_filter(context, filter, paging)
        except Exception as err:
            timing.end_failure(err)
        finally:
            timing.end_timing()

    def get_one_by_id(self, context: Optional[IContext], dummy_id: str) -> Dummy:
        timing = self._instrument(context, 'dummy.get_one_by_id')
        try:
            return self._controller.get_one_by_id(context, dummy_id)
        except Exception as err:
            timing.end_failure(err)
        finally:
            timing.end_timing()

    def create(self, context: Optional[IContext], item: Dummy) -> Dummy:
        timing = self._instrument(context, 'dummy.create')
        try:
            return self._controller.create(context, item)
        except Exception as err:
            timing.end_failure(err)
        finally:
            timing.end_timing()

    def update(self, context: Optional[IContext], item: Dummy) -> Dummy:
        timing = self._instrument(context, 'dummy.update')
        try:
            return self._controller.update(context, item)
        except Exception as err:
            timing.end_failure(err)
        finally:
            timing.end_timing()

    def delete_by_id(self, context: Optional[IContext], dummy_id: str) -> Dummy:
        timing = self._instrument(context, 'dummy.delete_by_id')
        try:
            return self._controller.delete_by_id(context, dummy_id)
        except Exception as err:
            timing.end_failure(err)
        finally:
            timing.end_timing()

    def check_trace_id(self, context: Optional[IContext]) -> str:
        timing = self._instrument(context, 'dummy.check_trace_id')
        try:
            return self._controller.check_trace_id(context)
        except Exception as err:
            timing.end_failure(err)
        finally:
            timing.end_timing()
