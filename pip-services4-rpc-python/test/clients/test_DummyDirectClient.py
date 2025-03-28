# -*- coding: utf-8 -*-
"""
    tests.rest.test_DummyDirectClient
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_components.refer import References, Descriptor

from .DummyClientFixture import DummyClientFixture
from .DummyDirectClient import DummyDirectClient
from test.sample.DummyService import DummyService


class TestDummyDirectClient:
    fixture = None
    client = None

    @classmethod
    def setup_class(cls):
        service = DummyService()

        cls.client = DummyDirectClient()

        references = References.from_tuples(
            Descriptor("pip-services-dummies", "service", "default", "default", "1.0"), service,
        )
        cls.client.set_references(references)

        cls.fixture = DummyClientFixture(cls.client)

    def setup_method(self, method):
        self.client.open(None)

    def teardown_method(self, method):
        self.client.close(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()
