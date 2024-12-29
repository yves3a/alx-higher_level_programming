#!/usr/bin/python3
"""8-base_geometry module."""


class BaseGeometry:
    """Define an empty class."""

    def area(self):
        """Define method area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define integer_validator.

        Args:
        name(str): The name
        value(int): The integer to be valiadated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        def area(self):
            """
            Calculates the area of a rectangle.
            Returns:
                int: The calculated area of the rectangle.
            """
            return self.__width * self.__height

        def str():
            """
            Return a string representation of the rectangle.

            Returns:
                str: The string representation of the rectangle.
            """
            return f"[Rectangle] {width}/{height}"
