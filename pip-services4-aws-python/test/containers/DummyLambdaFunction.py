# -*- coding: utf-8 -*-
from pip_services4_commons.convert import TypeCode
from pip_services4_components.refer import Descriptor, IReferences
from pip_services4_data.query import DataPage, FilterParams, PagingParams
from pip_services4_data.validate import ObjectSchema, FilterParamsSchema, PagingParamsSchema

from pip_services4_aws.containers.LambdaFunction import LambdaFunction
from test.Dummy import Dummy
from test.DummyFactory import DummyFactory
from test.DummySchema import DummySchema
from test.IDummyService import IDummyService


class DummyLambdaFunction(LambdaFunction):
    _service: IDummyService = None

    def __init__(self):
        super(DummyLambdaFunction, self).__init__("dummy", "Dummy lambda function")
        self._dependency_resolver.put('service',
                                      Descriptor('pip-services-dummies', 'service', 'default', '*', '*'))
        self._factories.add(DummyFactory())

    def set_references(self, references: IReferences):
        super().set_references(references)
        self._service = self._dependency_resolver.get_one_required('service')

    def __get_page_by_filter(self, params: dict) -> DataPage:
        return self._service.get_page_by_filter(
            params.get('trace_id'),
            FilterParams(params['filter']),
            PagingParams(params['paging'])
        )

    def __get_one_by_id(self, params: dict) -> Dummy:
        return self._service.get_one_by_id(
            params.get('trace_id'),
            params.get('dummy_id')
        )

    def __create(self, params: dict) -> Dummy:
        return self._service.create(
            params.get('trace_id'),
            params['dummy']
        )

    def __update(self, params: dict):
        return self._service.update(
            params.get('trace_id'),
            params['dummy']
        )

    def __delete_by_id(self, params: dict):
        return self._service.delete_by_id(
            params.get('trace_id'),
            params['dummy_id']
        )

    def register(self):
        self._register_action(
            'get_dummies',
            ObjectSchema(True).with_optional_property("filter", FilterParamsSchema())
                .with_optional_property("paging", PagingParamsSchema()),
            self.__get_page_by_filter
        )

        self._register_action(
            'get_dummy_by_id',
            ObjectSchema(True)
                .with_optional_property("dummy_id", TypeCode.String),
            self.__get_one_by_id
        )

        self._register_action(
            'create_dummy',
            ObjectSchema(True)
                .with_required_property("dummy", DummySchema()),
            self.__create
        )

        self._register_action(
            'update_dummy',
            ObjectSchema(True)
                .with_required_property("dummy", DummySchema()),
            self.__update
        )

        self._register_action(
            'delete_dummy',
            ObjectSchema(True)
                .with_optional_property("dummy_id", TypeCode.String),
            self.__delete_by_id
        )
