#!/usr/bin/python3
"""
Module for add_attribute method
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible

    Args:
        obj: The object to add attribute to
        attribute: The name of attribute to add
        value: The value of attribute

        Raises:
            TypeError: If the object can't have new attributes
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
