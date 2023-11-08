# -*- coding: utf-8 -*-

import threading

from pip_services4_data.keys import IdGenerator
from pip_services4_data.query import FilterParams, PagingParams, DataPage
from pip_services4_rpc.commands import ICommandable

from .DummyCommandSet import DummyCommandSet
from .IDummyService import IDummyService


class DummyService(IDummyService, ICommandable):
    _lock = None
    _items = None
    _command_set = None

    def __init__(self):
        self._lock = threading.Lock()
        self._items = []

    def get_command_set(self):
        if self._command_set is None:
            self._command_set = DummyCommandSet(self)
        return self._command_set

    def get_page_by_filter(self, context, filters, paging):
        filters = filters if filters is not None else FilterParams()
        key = filters.get_as_nullable_string("key")

        paging = paging if not (paging is None) else PagingParams()
        skip = paging.get_skip(0)
        take = paging.get_take(100)

        result = []
        self._lock.acquire()
        try:
            for item in self._items:
                if not (key is None) and key != item['key']:
                    continue

                skip -= 1
                if skip >= 0: continue

                take -= 1
                if take < 0: break

                result.append(item)
        finally:
            self._lock.release()

        return DataPage(result)

    def get_one_by_id(self, context, id):
        self._lock.acquire()
        try:
            for item in self._items:
                if item['dummy_id'] == id:
                    return item
        finally:
            self._lock.release()

        return None

    def create(self, context, item):
        self._lock.acquire()
        try:
            if 'dummy_id' not in item or item['dummy_id'] is None:
                item['dummy_id'] = IdGenerator.next_long()

            self._items.append(item)
        finally:
            self._lock.release()

        return item

    def update(self, context, new_item):
        self._lock.acquire()
        try:
            for index in range(len(self._items)):
                item = self._items[index]
                if item['dummy_id'] == new_item['dummy_id']:
                    self._items[index] = new_item
                    return new_item
        finally:
            self._lock.release()

        return None

    def delete_by_id(self, context, id):
        self._lock.acquire()
        try:
            for index in range(len(self._items)):
                item = self._items[index]
                if item['dummy_id'] == id:
                    del self._items[index]
                    return item
        finally:
            self._lock.release()

        return None
