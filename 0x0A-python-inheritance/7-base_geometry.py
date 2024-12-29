#!/usr/bin/python3
"""
Represents class BaseGeometry
"""


class BaseGeometry:
    """
    A class raises an exception
    """

    def area(self):
        """
        Define a mothod area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Define integer_validator


        Args:
        name(str): The name
        value(int): The integer to be valiadated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
