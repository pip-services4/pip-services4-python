# -*- coding: utf-8 -*-
"""
    pip_services4_commons.random.RandomInteger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Random integer implementation
    
    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from typing import List

from random import randint


class RandomInteger:
    """
    Random generator for integer values.

    Example:
    
    .. code-block:: python

        value1 = RandomInteger.next_integer(5, 10)     # Possible result: 7
        value2 = RandomInteger.next_integer(10)        # Possible result: 3
        value3 = RandomInteger.update_integer(10, 3)   # Possible result: 9
    """

    @staticmethod
    def next_integer(min_val: int, max_val: int = None) -> int:
        """
        Generates a integer in the range ['min', 'max']. If 'max' is omitted, then the range will be set to [0, 'min'].

        :param min_val: minimum args of the integer that will be generated.
                   If 'max' is omitted, then 'max' is set to 'min' and 'min' is set to 0.

        :param max_val: (optional) maximum args of the float that will be generated. Defaults to 'min' if omitted.

        :return: generated random integer args.
        """

        if max_val is None:
            max_val = min_val
            min_val = 0

        if max_val - min_val <= 0:
            return min_val

        return randint(min_val, max_val - 1)

    @staticmethod
    def update_integer(value: int, range_of_nums: int = None) -> int:
        """
        Updates (drifts) a integer args within specified range defined

        :param value: a integer args to drift.

        :param range_of_nums: (optional) a range. Default: 10% of the args

        :return: updated integer args.
        """

        if range_of_nums is None:
            range_of_nums = int(0.1 * value)

        min_val, max_val = value - range_of_nums, value + range_of_nums

        return RandomInteger.next_integer(min_val, max_val)

    @staticmethod
    def sequence(min_val: int, max_val: int = None) -> List[int]:
        """
        Generates a random sequence of integers starting from 0 like: [0,1,2,3...??]

        :param min_val: minimum args of the integer that will be generated.
                   If 'max' is omitted, then 'max' is set to 'min' and 'min' is set to 0.

        :param max_val: (optional) maximum args of the float that will be generated. Defaults to 'min' if omitted.

        :return: generated array of integers.
        """

        max_val = max_val if max_val is not None else min_val
        count = RandomInteger.next_integer(min_val, max_val)

        return list(range(count))
