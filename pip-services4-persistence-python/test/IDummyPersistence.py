# -*- coding: utf-8 -*-
"""
    test.IDummyPersistence
    ~~~~~~~~~~~~~~~~~~~~~~
    
    Interface for dummy persistence components
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_persistence.read import IGetter
from pip_services4_persistence.write.IPartialUpdater import IPartialUpdater
from pip_services4_persistence.write.IWriter import IWriter


class IDummyPersistence(IGetter, IWriter, IPartialUpdater):

    def get_page_by_filter(self, context, filter, paging):
        raise NotImplementedError('Method from interface definition')

    def get_one_by_id(self, context, id):
        raise NotImplementedError('Method from interface definition')

    def create(self, context, entity):
        raise NotImplementedError('Method from interface definition')

    def update(self, context, entity):
        raise NotImplementedError('Method from interface definition')

    def update_partially(self, context, id, data):
        raise NotImplementedError('Method from interface definition')

    def delete_by_id(self, context, id):
        raise NotImplementedError('Method from interface definition')
