# -*- coding: utf-8 -*-
"""
    pip_services4_commons.random.RandomString
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    RandomString implementation
    
    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from random import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from typing import List

from .RandomBoolean import RandomBoolean
from .RandomInteger import RandomInteger


class RandomString(object):
    """
    Random generator for string values.

    Example:
    
    .. code-block:: python

        value1 = RandomString.pickChar("ABC")     # Possible result: "C"
        value2 = RandomString.pick(["A","B","C"]) # Possible result: "gBW"
    """

    @staticmethod
    def pick(values: List[str]) -> str:
        """
        Picks a random string from an array of string.

        :param values: a string to pick from

        :return: a randomly picked string.
        """
        if values is None or len(values) == 0:
            return ''

        return choice(values)

    @staticmethod
    def pick_char(values: str) -> str:
        """
        Picks a random character from a string.

        :param values: a string to pick a char from

        :return: a randomly picked char.
        """
        if values is None or len(values) == 0:
            return ''
        index = RandomInteger.next_integer(len(values))
        return values[index]

    @staticmethod
    def distort(value: str) -> str:
        """
        Distorts a string by randomly replacing characters in it.

        :param value: a string to distort.

        :return: a distored string.
        """
        value = value.lower()

        if RandomBoolean.chance(1, 5):
            value = value[0:1].upper() + value[1:]

        if RandomBoolean.chance(1, 3):
            value = value + choice(punctuation)

        return value

    @staticmethod
    def next_alpha_char() -> str:
        """
        Generates random alpha characted [A-Za-z]
        :return: a random characted.
        """
        return choice("".join((ascii_uppercase, ascii_lowercase)))

    @staticmethod
    def next_string(min_size: int, max_size: int) -> str:
        """
        Generates a random string, consisting of upper and lower case letters (of the English alphabet),
        digits (0-9), and symbols ("_,.:-/.[].{},#-!,$=%.+^.&*-() ").

        :param min_size: (optional) minimum string length.

        :param max_size: maximum string length.

        :return: a random string.
        """
        result = ""

        max_size = max_size if max_size is not None else min_size
        length = RandomInteger.next_integer(min_size, max_size)
        for i in range(length):
            result += choice("".join((ascii_uppercase, ascii_lowercase, digits, punctuation)))

        return result
