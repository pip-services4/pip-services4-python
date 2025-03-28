# -*- coding: utf-8 -*-
"""
    test.DummyCommandSet
    ~~~~~~~~~~~~~~~~~~~~

    Dummy command set

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from typing import Optional

from pip_services4_commons.convert import TypeCode
from pip_services4_components.exec import Parameters
from pip_services4_components.context import IContext
from pip_services4_data.query import FilterParams, PagingParams
from pip_services4_data.validate import ObjectSchema, FilterParamsSchema, PagingParamsSchema

from pip_services4_rpc.commands import Command, CommandSet, ICommand


from test.sample import IDummyService, Dummy
from test.sample.DummySchema import DummySchema


class DummyCommandSet(CommandSet):
    _service: IDummyService

    def __init__(self, service):
        super(DummyCommandSet, self).__init__()

        self._service = service

        self.add_command(self._make_get_page_by_filter_command())
        self.add_command(self._make_get_one_by_id_command())
        self.add_command(self._make_create_command())
        self.add_command(self._make_update_command())
        self.add_command(self._make_delete_by_id_command())
        self.add_command(self._make_check_trace_id())

    def _make_get_page_by_filter_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters):
            filter = FilterParams.from_value(args.get("filter"))
            paging = PagingParams.from_value(args.get("paging"))
            page = self._service.get_page_by_filter(context, filter, paging)
            return page

        return Command(
            "get_dummies",
            ObjectSchema(True).with_optional_property("filter", FilterParamsSchema()).with_optional_property(
                "paging", PagingParamsSchema()),
            handler
        )

    def _make_get_one_by_id_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters):
            id = args.get_as_string("dummy_id")
            return self._service.get_one_by_id(context, id)

        return Command(
            "get_dummy_by_id",
            ObjectSchema(True).with_required_property("dummy_id", TypeCode.String), handler)

    def _make_create_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters):
            entity = args.get("dummy")
            if isinstance(entity, dict):
                entity = Dummy.from_json(entity)
            return self._service.create(context, entity)

        return Command(
            "create_dummy",
            ObjectSchema(True).with_required_property("dummy", DummySchema()),
            handler
        )

    def _make_update_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters):
            entity = args.get("dummy")
            if isinstance(entity, dict):
                entity = Dummy.from_json(entity)
            return self._service.update(context, entity)

        return Command(
            "update_dummy",
            ObjectSchema(True).with_required_property("dummy", DummySchema()),
            handler
        )

    def _make_delete_by_id_command(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters):
            id = args.get_as_string("dummy_id")
            return self._service.delete_by_id(context, id)

        return Command(
            "delete_dummy",
            ObjectSchema(True).with_required_property("dummy_id", TypeCode.String),
            handler
        )

    def _make_check_trace_id(self) -> ICommand:
        def handler(context: Optional[IContext], args: Parameters):
            value = self._service.check_trace_id(context)
            return {'trace_id': value}

        return Command(
            "check_trace_id",
            ObjectSchema(True),
            handler
        )
