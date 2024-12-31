#!/usr/bin/python3
"""
Represents class that inherits from BaseGeometry class
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


class Rectangle(BaseGeometry):
    """
    A class that inherits from class BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Both are validated as positive integers.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
        self.integer_validator("height", height)
