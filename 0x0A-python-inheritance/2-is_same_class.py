#!/usr/bin/python3
"""
Function that checks if the object is exactly instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Function that checks if the object is exactly an instance of a class
    """
    return type(obj) is a_class
