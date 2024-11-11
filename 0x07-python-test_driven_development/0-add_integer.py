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
    match (isinstance(a, (int, float)), isinstance(b, (int, float))):
        case (False, _):
            raise TypeError("a must be an integer")
        case (_, False):
            raise TypeError("b must be an integer")
        case _:
            pass

    return int(a) + int(b)
