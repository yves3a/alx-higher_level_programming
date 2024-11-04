#!/usr/bin/python3
"""
Module
Defines a class with private instance attribute size
"""


class Square:
    """Square class with a private instance attribute size."""

    def __init__(self, size=0):
        """
        Initializes the class with a private instance attribute size.

        Args:
            size (int): The size of the side, must be an integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size

        Args:
            value (int): The value to be assigned to size, must be an integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
