#!/usr/bin/python3
"""
A funct that returns True f the object is an instance of
a class that inherited from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of
    a class that inherited from the specified class ; otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
