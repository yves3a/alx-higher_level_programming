#!/usr/bin/python3
"""
Module that
Returns the addition of two integers.
"""


def add_integer(a, b=98):
    """Returns addition of two integers
    Args:
    a: the first integer
    b: second integer

    Raises:
    TypeError: when a or b are not int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
