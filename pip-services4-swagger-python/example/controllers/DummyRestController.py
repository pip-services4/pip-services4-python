# -*- coding: utf-8 -*-
import json
import pathlib

import bottle
from pip_services4_commons.convert import TypeCode
from pip_services4_components.context import Context
from pip_services4_components.refer import Descriptor
from pip_services4_data.query import PagingParams, FilterParams
from pip_services4_data.validate import ObjectSchema
from pip_services4_http.controller import RestController

from data.DummySchema import DummySchema
from logic.IDummyService import IDummyService


class DummyRestController(RestController):
    def __init__(self):
        super(DummyRestController, self).__init__()
        self._dependency_resolver.put('service',
                                      Descriptor("pip-services", "service", "default", "*", "*"))

        self._controller: IDummyService = None

    def configure(self, config):
        super().configure(config)

    def set_references(self, references):
        super().set_references(references)
        self._controller = self._dependency_resolver.get_one_required('service')

    def __get_page_by_filter(self):
        paging = PagingParams(bottle.request.query.get('skip'),
                              bottle.request.query.get('take'),
                              bottle.request.query.get('total'))
        filter = FilterParams(bottle.request.query.dict)

        return self.send_result(
            self._controller.get_page_by_filter(Context.from_trace_id(bottle.request.query.get('trace_id')), filter, paging))

    def __get_one_by_id(self, dummy_id):
        return self.send_result(self._controller.get_one_by_id(
            Context.from_trace_id(bottle.request.query.get('trace_id')),
            dummy_id,
        ))

    def __create(self):
        return self.send_created_result(self._controller.create(
            Context.from_trace_id(bottle.request.query.get('trace_id')),
            json.loads(bottle.request.json).get('body'),
        ))

    def __update(self):
        return self.send_result(self._controller.update(
            Context.from_trace_id(bottle.request.query.get('trace_id')),
            json.loads(bottle.request.json).get('body'),
        ))

    def __delete_by_id(self, dummy_id):
        return self.send_deleted_result(self._controller.delete_by_id(
            Context.from_trace_id(bottle.request.query.get('trace_id')),
            dummy_id,
        ))

    def register(self):
        self.register_route('get', '/dummies',
                            ObjectSchema(True)
                            .with_optional_property("skip", TypeCode.String)
                            .with_optional_property("take", TypeCode.String)
                            .with_optional_property("total", TypeCode.String),
                            self.__get_page_by_filter
                            )

        self.register_route('get', '/dummies/<dummy_id>',
                            ObjectSchema(True)
                            .with_required_property("dummy_id", TypeCode.String),
                            self.__get_one_by_id)

        self.register_route('post', '/dummies', ObjectSchema(True)
                            .with_required_property("body", DummySchema()),
                            self.__create)

        self.register_route('put', '/dummies/<dummy_id>',
                            ObjectSchema(True)
                            .with_required_property("body", DummySchema()),
                            self.__update)

        self.register_route('delete', '/dummies/<dummy_id>',
                            ObjectSchema(True)
                            .with_required_property("dummy_id", TypeCode.String),
                            self.__delete_by_id)

        self._swagger_route = '/dummies/swagger'
        self._register_open_api_spec_from_file(
            str(pathlib.Path(__file__).parent) + '/../../example/controllers/dummy.yml')
