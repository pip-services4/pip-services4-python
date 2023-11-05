# -*- coding: utf-8 -*-
from typing import Optional

from pip_services4_commons.convert import TypeCode
from pip_services4_data.query import FilterParams, PagingParams
from pip_services4_data.validate import ObjectSchema, PagingParamsSchema, FilterParamsSchema
from pip_services4_rpc.commands import ICommand, CommandSet, Command

from pip_services4_components.exec import Parameters

from pip_services4_components.context import IContext

from .Dummy import Dummy
from .DummySchema import DummySchema
from .IDummyService import IDummyService


class DummyCommandSet(CommandSet):

    def __init__(self, controller: IDummyService):
        super(DummyCommandSet, self).__init__()

        self.__controller: IDummyService = controller

        self.add_command(self.__make_get_page_by_filter_command())
        self.add_command(self.__make_get_one_by_id_command())
        self.add_command(self.__make_create_command())
        self.add_command(self.__make_update_command())
        self.add_command(self.__make_delete_by_id_command())

    def __make_get_page_by_filter_command(self) -> ICommand:
        def command_func(context: Optional[str], args: Parameters):
            filter = FilterParams.from_value(args.get("filter"))
            paging = PagingParams.from_value(args.get("paging"))
            page = self.__controller.get_page_by_filter(context, filter, paging)

            if len(page.data) > 0:
                serealized_items = []
                for item in page.data:
                    serealized_items.append(item.to_dict())

                page = page.to_json()
                page['data'] = serealized_items

            return page

        return Command(
            "get_dummies",
            ObjectSchema(True).with_optional_property("filter", FilterParamsSchema())
                .with_optional_property("paging", PagingParamsSchema()),
            command_func
        )

    def __make_get_one_by_id_command(self) -> ICommand:
        def command_func(context: Optional[IContext], args: Parameters):
            id = args.get_as_string("dummy_id")
            res = self.__controller.get_one_by_id(context, id)
            if res:
                return res.to_dict()
            return ''

        return Command(
            "get_dummy_by_id",
            ObjectSchema(True).with_required_property("dummy_id", TypeCode.String),
            command_func
        )

    def __make_create_command(self) -> ICommand:
        def command_func(context: Optional[IContext], args: Parameters):
            entity: Dummy = None if 'dummy' not in args.keys() else Dummy(**args['dummy'])
            res: Dummy = self.__controller.create(context, entity)
            if res:
                return res.to_dict()
            return ''

        return Command(
            "create_dummy",
            ObjectSchema(True).with_required_property("dummy", DummySchema()),
            command_func
        )

    def __make_update_command(self) -> ICommand:
        def command_func(context: Optional[IContext], args: Parameters):
            entity: Dummy = None if 'dummy' not in args.keys() else Dummy(**args['dummy'])
            res = self.__controller.update(context, entity)
            if res:
                return res.to_dict()
            return ''

        return Command(
            "update_dummy",
            ObjectSchema(True).with_required_property("dummy", DummySchema()),
            command_func
        )

    def __make_delete_by_id_command(self) -> ICommand:
        def command_func(context: Optional[IContext], args: Parameters):
            id = args.get_as_string("dummy_id")
            res = self.__controller.delete_by_id(context, id)
            if res:
                return res.to_dict()
            return ''

        return Command(
            "delete_dummy",
            ObjectSchema(True).with_required_property("dummy_id", TypeCode.String),
            command_func
        )
