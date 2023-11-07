# -*- coding: utf-8 -*-
from pip_services4_commons.convert import TypeCode
from pip_services4_data.query import PagingParams, FilterParams, DataPage
from pip_services4_data.validate import ObjectSchema, FilterParamsSchema, PagingParamsSchema
from pip_services4_rpc.commands import CommandSet, ICommand, Command

from .Dummy import Dummy
from .DummySchema import DummySchema
from .IDummyService import IDummyService


class DummyCommandSet(CommandSet):

    def __init__(self, service: IDummyService):
        super().__init__()
        self.__service = service

        self.add_command(self.__make_page_by_filter_command())
        self.add_command(self._make_get_one_by_id_command())
        self.add_command(self._make_create_command())
        self.add_command(self._make_update_command())
        self.add_command(self._make_delete_by_id_command())

    def __make_page_by_filter_command(self) -> ICommand:
        def handler(context, args):
            filter = FilterParams.from_value(args.get("filter"))
            paging = PagingParams.from_value(args.get("paging"))

            response = self.__service.get_page_by_filter(context, filter, paging)

            items = []
            for item in response.data:
                items.append(Dummy.to_dict(item))

            return DataPage(items, len(items))

        return Command(
            'get_dummies',
            ObjectSchema().with_optional_property(
                'filter', FilterParamsSchema()).with_optional_property(
                'paging', PagingParamsSchema()),
            handler
        )

    def _make_get_one_by_id_command(self):
        def handler(context, args):
            id = args.get_as_string("dummy_id")
            result = self.__service.get_one_by_id(context, id)
            return None if not result.id else Dummy.to_dict(result)

        return Command(
            "get_dummy_by_id",
            ObjectSchema().with_required_property('dummy_id', TypeCode.String),
            handler
        )

    def _make_create_command(self):
        def handler(context, args):
            entity = args.get("dummy")
            result = self.__service.create(context, Dummy(**entity))
            return Dummy.to_dict(result)

        return Command(
            "create_dummy",
            ObjectSchema().with_required_property('dummy', DummySchema()),
            handler
        )

    def _make_update_command(self):
        def handler(context, args):
            entity = args.get("dummy")
            result = self.__service.update(context, Dummy(**entity))
            return Dummy.to_dict(result)

        return Command(
            "update_dummy",
            ObjectSchema().with_required_property('dummy', DummySchema()),
            handler
        )

    def _make_delete_by_id_command(self):
        def handler(context, args):
            id = args.get_as_string("dummy_id")
            result = self.__service.delete_by_id(context, id)
            return Dummy.to_dict(result)

        return Command(
            "delete_dummy",
            ObjectSchema().with_required_property('dummy_id', TypeCode.String),
            handler
        )
