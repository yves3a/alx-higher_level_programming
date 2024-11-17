#!/usr/bin/python3
"""Represent a rectangle"""


class Rectangle:
    """Creating a new rectangle"""
    def __init__(self, width=0, height=0):
        """Initialising a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retreiving height"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retreiving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height value"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns an area of the rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        """Represents the perimenter of the rectangle"""
        if self.__width == 0 and self.__height == 0:
            return 0
        else:
            return (
                2 * (self.__width + self.__height)
                if self.width and self.height else 0
            )

    def __str__(self):
        """Returns printable string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)
