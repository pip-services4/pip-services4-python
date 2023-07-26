# -*- coding: utf-8 -*-
"""
    test.memory.DummyMemoryPersistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Dummy memory persistence implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_persistence.persistence import IdentifiableMemoryPersistence
from pip_services4_persistence.write.IPartialUpdater import IPartialUpdater
from pip_services4_data.query.FilterParams import FilterParams


class DummyMemoryPersistence(IdentifiableMemoryPersistence, IPartialUpdater):

    def __init__(self):
        super(DummyMemoryPersistence, self).__init__()

    def get_page_by_filter(self, context, filter, paging):
        filter = filter if filter is not None else FilterParams()
        key = filter.get_as_nullable_string("key")

        def filter_dummy(obj):
            if key != None and obj['key'] != key:
                return False
            return True

        return super(DummyMemoryPersistence, self).get_page_by_filter(context, filter_dummy, paging=paging)
