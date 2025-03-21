# -*- coding: utf-8 -*-
from pip_services4_data.data import IStringIdentifiable


class Dummy(IStringIdentifiable):

    def __init__(self, id: str = None, key: str = None, content: str = None):
        self.id = id
        self.key = key
        self.content = content

    def clone(self):
        return Dummy(self.id, self.key, self.content)

    @staticmethod
    def to_dict(dummy: 'Dummy') -> dict:
        if dummy is not None:
            return {'id': dummy.id, 'key': dummy.key, 'content': dummy.content}
