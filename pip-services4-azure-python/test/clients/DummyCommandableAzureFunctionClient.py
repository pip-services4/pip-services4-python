# -*- coding: utf-8 -*-
from typing import Optional

from pip_services4_components.context import IContext
from pip_services4_data.query import FilterParams, PagingParams, DataPage

from pip_services4_azure.clients import CommandableAzureFunctionClient
from test.Dummy import Dummy
from test.IDummyClient import IDummyClient


class DummyCommandableAzureFunctionClient(CommandableAzureFunctionClient, IDummyClient):

    def __init__(self):
        super().__init__('dummies')

    def get_dummies(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        response = self.call_command('get_dummies', context, {'filter': filter, 'paging': paging.to_json()})

        items = []
        for item in response['data']:
            items.append(Dummy(**item))
        return DataPage(items)

    def get_dummy_by_id(self, context: Optional[IContext], id: str) -> Optional[Dummy]:
        response = self.call_command('get_dummy_by_id', context, {'dummy_id': id})

        if not response:
            return None

        return Dummy(**response)

    def create_dummy(self, context: Optional[IContext], entity: Dummy) -> Dummy:
        response = self.call_command('create_dummy', context, {'dummy': entity.to_dict()})
        return Dummy(**response)

    def update_dummy(self, context: Optional[IContext], entity: Dummy) -> Dummy:
        response = self.call_command('update_dummy', context, {'dummy': entity.to_dict()})

        return Dummy(**response)

    def delete__dummy(self, context: Optional[IContext], id: str) -> Dummy:
        response = self.call_command('delete_dummy', context, {'dummy_id': id})

        return Dummy(**response)
