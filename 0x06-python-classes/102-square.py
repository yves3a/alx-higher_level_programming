#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (number): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (number): The size to set.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define the > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Define the < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison"""
        return self.area() <= other.area()
