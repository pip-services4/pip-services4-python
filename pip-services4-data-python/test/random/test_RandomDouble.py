# -*- coding: utf-8 -*-
from pip_services4_data.random import RandomDouble


class TestRandomDouble:

    def test_next_double(self):
        value = RandomDouble.next_double(5)
        assert value <= 5

        value = RandomDouble.next_double(2, 5)
        assert 5 >= value >= 2

    def test_update_double(self):
        value = RandomDouble.update_double(0, 5)
        assert 5 >= value >= -5

        value = RandomDouble.update_double(5, 0)

        value = RandomDouble.update_double(0)
        assert value == 0
