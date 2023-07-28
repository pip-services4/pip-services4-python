# -*- coding: utf-8 -*-
"""
    pip_services4_rpc.clients.__init__
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Clients module implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

__all__ = ['DummyClientFixture', 'DummyDirectClient'
'IDummyClient', 'TestDummyDirectClient']

from .DummyClientFixture import DummyClientFixture
from .DummyDirectClient import DummyDirectClient
from .IDummyClient import IDummyClient
from .test_DummyDirectClient import TestDummyDirectClient
