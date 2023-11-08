# -*- coding: utf-8 -*-
from pip_services4_commons.convert import TypeCode
from pip_services4_data.query import FilterParams, PagingParams
from pip_services4_data.validate import ObjectSchema, FilterParamsSchema, PagingParamsSchema
from pip_services4_rpc.commands import CommandSet, Command

from data.DummySchema import DummySchema
from .IDummyService import IDummyService


class DummyCommandSet(CommandSet):

    def __init__(self, service: IDummyService):
        super(DummyCommandSet, self).__init__()

        self._service = service

        self.add_command(self.__make_get_page_by_filter_command())
        self.add_command(self.__make_get_one_by_id_command())
        self.add_command(self.__make__create_command())
        self.add_command(self.__make__update_command())
        self.add_command(self.__make_delete_by_id_command())

    def __make_get_page_by_filter_command(self):
        def callback(context, args):
            filter = FilterParams.from_value(args.get('filter'))
            paging = PagingParams.from_value(args.get('paging'))
            return self._service.get_page_by_filter(context, filter, paging)

        return Command(
            'get_dummies',
            ObjectSchema(True)
                .with_optional_property("filter", FilterParamsSchema())
                .with_optional_property("paging", PagingParamsSchema()),
            callback
        )

    def __make_get_one_by_id_command(self):
        def callback(context, args):
            id = args.get_as_string('dummy_id')
            return self._service.get_one_by_id(context, id)

        return Command(
            'get_dummy_by_id',
            ObjectSchema(True).with_required_property('dummy_id', TypeCode.String),
            callback
        )

    def __make__create_command(self):
        def callback(context, args):
            entity = args.get('dummy')
            return self._service.create(context, entity)

        return Command(
            'create_dummy',
            ObjectSchema(True).with_required_property('dummy', DummySchema()),
            callback
        )

    def __make__update_command(self):
        def callback(context, args):
            entity = args.get('dummy')
            return self._service.update(context, entity)

        return Command(
            'update_dummy',
            ObjectSchema(True).with_required_property('dummy', DummySchema()),
            callback
        )

    def __make_delete_by_id_command(self):
        def callback(context, args):
            id = args.get('dummy_id')
            return self._service.delete_by_id(context, id)

        return Command(
            'delete_dummy',
            ObjectSchema(True).with_required_property('dummy_id', TypeCode.String),
            callback
        )
