# -*- coding: utf-8 -*-
import threading
from typing import List, Optional

from pip_services4_components.context import IContext
from pip_services4_data.keys import IdGenerator
from pip_services4_data.query import FilterParams, PagingParams, DataPage
from pip_services4_rpc.commands import ICommandable, CommandSet

from .Dummy import Dummy
from .DummyCommandSet import DummyCommandSet
from .IDummyService import IDummyService
from .protos import dummies_pb2


class DummyService(IDummyService, ICommandable):

    def __init__(self):
        self._lock = threading.Lock()
        self.__entities: List[Dummy] = []
        self.__command_set: DummyCommandSet = None

    def get_command_set(self) -> CommandSet:
        if self.__command_set is None:
            self.__command_set = DummyCommandSet(self)
        return self.__command_set

    def get_page_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        filter = filter if filter is not None else FilterParams()
        key = filter.get_as_nullable_string("key")

        paging = paging if paging is not None else PagingParams()
        skip = paging.get_skip(0)
        take = paging.get_take(100)

        result = dummies_pb2.DummiesPage()

        for item in self.__entities:
            if key is not None and key != item.key:
                continue

            skip -= 1
            if skip >= 0:
                continue

            take -= 1
            if take < 0:
                break

            if not isinstance(item, dummies_pb2.Dummy):
                pb2_item = dummies_pb2.Dummy()
                pb2_item.id = item.id
                pb2_item.content = item.content
                pb2_item.key = item.key
                item = pb2_item

            result.data.append(item)

        result.total = len(result.data)

        return result

    def get_one_by_id(self, context: Optional[IContext], id: str) -> Optional[Dummy]:
        self._lock.acquire()
        try:
            for item in self.__entities:
                if item.id == id:
                    return item
        finally:
            self._lock.release()

        return dummies_pb2.Dummy()

    def create(self, context: Optional[str], item: Dummy) -> Dummy:
        self._lock.acquire()
        try:
            if item.id == '' or item.id is None:
                item.id = IdGenerator.next_long()

            self.__entities.append(item)
        finally:
            self._lock.release()

        return item

    def update(self, context: Optional[IContext], new_item: Dummy) -> Optional[Dummy]:
        self._lock.acquire()
        try:
            for index in range(len(self.__entities)):
                item = self.__entities[index]
                if item.id == new_item.id:
                    self.__entities[index] = new_item
                    return new_item
        finally:
            self._lock.release()

        return dummies_pb2.Dummy()

    def delete_by_id(self, context: Optional[IContext], id: str) -> Optional[Dummy]:
        self._lock.acquire()
        try:
            for index in range(len(self.__entities)):
                item = self.__entities[index]
                if item.id == id:
                    del self.__entities[index]
                    return item
        finally:
            self._lock.release()

        return dummies_pb2.Dummy()
