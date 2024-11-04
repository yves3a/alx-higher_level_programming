#!/usr/bin/python3
"""
Module that defines a Square class with a private instance attribute size.
"""


class Square:
    """Square class with a private instance attribute size."""

    def __init__(self, size=0):
        """
        Initializes the square with a private size.

        Args:
            size (int): The size of the side, must be an integer.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self.size = size  # Invoking the setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size of the square.

        Args:
            value (int): The value to be assigned to size, must be an integer.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
