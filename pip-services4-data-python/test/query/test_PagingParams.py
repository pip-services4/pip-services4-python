# -*- coding: utf-8 -*-
from pip_services4_data.query import PagingParams


class TestPagingParams:

    def test_create_empty_PagingParams_regular(self):
        paging = PagingParams()
        assert paging.skip is None
        assert paging.take is None
        assert paging.total is False

    def test_create_empty_PagingParams_gRPC(self):
        paging = PagingParams(0, 0, False)
        assert 0 == paging.skip
        assert paging.take is None
        assert paging.total is False

    def test_create_PagingParams_with_set_skip_take_values(self):
        paging = PagingParams(25, 50, False)
        assert 25 == paging.skip
        assert 50 == paging.take
        assert paging.total is False

    def test_get_skip_and_get_take(self):
        paging = PagingParams(25, 50, False)
        assert 50 == paging.get_skip(50)
        assert 25 == paging.get_skip(10)
        assert 50 == paging.get_take(100)
        assert 25 == paging.get_take(25)

        paging = PagingParams()
        assert 10 == paging.get_skip(10)
        assert 10 == paging.get_skip(10)
