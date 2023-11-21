# -*- coding: utf-8 -*-
from typing import Optional

from pip_services4_components.context import IContext
from pip_services4_data.query import FilterParams, PagingParams

from pip_services4_mysql.persistence.IdentifiableMySqlPersistence import IdentifiableMySqlPersistence
from test.fixtures.IDummyPersistence import IDummyPersistence


class DummyMySqlPersistence(IdentifiableMySqlPersistence, IDummyPersistence):
    def __init__(self):
        super(DummyMySqlPersistence, self).__init__('dummies')

    def _define_schema(self):
        self._clear_schema()
        self._ensure_schema(
            'CREATE TABLE `' + self._table_name + '` (id VARCHAR(32) PRIMARY KEY, `key` VARCHAR(50), `content` TEXT)')
        self._ensure_index(self._table_name + '_key', {'key': 1}, {'unique': True})

    def get_page_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams, sort=None,
                           select=None):
        filter = filter or FilterParams()
        key = filter.get_as_nullable_string('key')

        filter_condition = ''
        if key is not None:
            filter_condition += "`key`='" + key + "'"

        return super().get_page_by_filter(context, filter_condition, paging, None, None)

    def get_count_by_filter(self, context: Optional[IContext], filter: FilterParams):
        filter = filter or FilterParams()
        key = filter.get_as_nullable_string('key')

        filter_condition = ''
        if key is not None:
            filter_condition += "`key`='" + key + "'"

        return super().get_count_by_filter(context, filter_condition)
