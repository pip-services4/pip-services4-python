# -*- coding: utf-8 -*-
"""
    pip_services4_commons.random.RandomFloat
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    RandomFloat implementation
    
    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from random import random


class RandomFloat:
    """
    Random generator for float values.

    Example:

    .. code-block:: python

        value1 = RandomFloat.next_float(5, 10)     # Possible result: 7.3
        value2 = RandomFloat.next_float(10)        # Possible result: 3.7
        value3 = RandomFloat.update_float(10, 3)   # Possible result: 9.2
    """

    @staticmethod
    def next_float(min_val: float, max_val: float = None) -> float:
        if max_val is None:
            max_val, min_val = min_val, 0

        if max_val - min_val <= 0:
            return min_val

        return min_val + random() * (max_val - min_val)

    @staticmethod
    def update_float(value: float, range_of_nums: float = None) -> float:
        """
        Updates (drifts) a float args within specified range defined

        :param value: a float args to drift.

        :param range_of_nums: (optional) a range. Default: 10% of the args

        :return: updated random float args.
        """
        if range_of_nums is None:
            range_of_nums = 0.1 * value

        min_val, max_val = value - range_of_nums, value + range_of_nums

        return RandomFloat.next_float(min_val, max_val)
