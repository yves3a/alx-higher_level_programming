#!/usr/bin/python3
"""
Funct that returns True if object is an instance of or
an instance of a class that inherite from a specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is instance of or an instance of a
    class that inherite from a specified class
    """
    return isinstance(obj, a_class)
