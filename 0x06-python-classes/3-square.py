#!/usr/bin/python3
"""
Module 2-square
Defines a Square class with a private instance attribute size.
"""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes the square with a private size attribute.

        Args:
            size (int): The size of its side, which must be an integer.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that returns the area of a square"""
        return self.__size**2
