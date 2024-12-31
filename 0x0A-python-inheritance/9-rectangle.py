#!/usr/bin/python3
"""
A module that inherits from the BaseGeometry class and
models a Rectangle objects.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): the width of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

        def __str__():
            """
            Return a string representation of the rectangle.

            Returns:
                str: The string representation of the rectangle.
            """
            return f"[{type(self).__name__}] {self.__width}/{self.__height}"

        def area(self):
            """
            Calculates the area of a rectangle.
            Returns:
                int: The calculated area of the rectangle.
            """
            return self.__width * self.__height
