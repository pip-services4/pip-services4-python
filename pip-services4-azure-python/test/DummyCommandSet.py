# -*- coding: utf-8 -*-
import json
from typing import Optional

import azure.functions as func
from pip_services4_commons.convert import TypeCode

from pip_services4_components.context import IContext
from pip_services4_components.exec import Parameters
from pip_services4_data.query import DataPage, FilterParams, PagingParams
from pip_services4_data.validate import ObjectSchema, FilterParamsSchema, PagingParamsSchema
from pip_services4_rpc.commands import CommandSet, ICommand, Command

from test.Dummy import Dummy
from test.DummySchema import DummySchema
from test.IDummyService import IDummyService


class DummyCommandSet(CommandSet):
    __controller: IDummyService

    def __init__(self, controller: IDummyService):
        super().__init__()

        self.__controller = controller

        self.add_command(self.__make_get_page_by_filter_command())
        self.add_command(self.__make_get_one_by_id_command())
        self.add_command(self.__make_create_command())
        self.add_command(self.__make_update_command())
        self.add_command(self.__make_delete_by_id_command())

    def __make_get_page_by_filter_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters) -> DataPage:
            filter = FilterParams.from_value(args.get("filter"))
            paging = PagingParams.from_value(args.get('paging'))

            return self.__controller.get_page_by_filter(context, filter, paging)

        return Command(
            'get_dummies',
            ObjectSchema(True)
                .with_optional_property('filter', FilterParamsSchema())
                .with_optional_property('paging', PagingParamsSchema()),
            handler
        )

    def __make_get_one_by_id_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters) -> Dummy:
            id = args.get_as_string('dummy_id')
            return self.__controller.get_one_by_id(context, id)

        return Command(
            'get_dummy_by_id',
            ObjectSchema(True).with_required_property('dummy_id', TypeCode.String),
            handler
        )

    def __make_create_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters) -> Dummy:
            entity = args.get('dummy')
            if entity:
                return self.__controller.create(context, Dummy(**entity))

        return Command(
            'create_dummy',
            ObjectSchema(True).with_required_property('dummy', DummySchema()),
            handler
        )

    def __make_update_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters) -> Dummy:
            entity = args.get('dummy')
            if entity:
                return self.__controller.update(context, Dummy(**entity))

        return Command(
            'update_dummy',
            ObjectSchema(True).with_required_property('dummy', DummySchema()),
            handler
        )

    def __make_delete_by_id_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters) -> Dummy:
            id = args.get('dummy_id')
            if id:
                return self.__controller.delete_by_id(context, id)

        return Command(
            "delete_dummy",
            ObjectSchema(True).with_required_property('dummy_id', TypeCode.String),
            handler
        )
