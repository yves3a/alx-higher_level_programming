#!/usr/bin/python3
"""
Module
Defines a class with private instance attributes size and position
"""


class Square:
    """Square class with private instance attributes size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the class with private instance size and position.

        Args:
            size(int): The size of the side, must be an integer.
            position(tuple): The position must be a tuple of 2 positive int.

        Raises:
            TypeError: If size is not int or position is not a tuple of 2 int.
            ValueError: If size is less than 0 or position contains neg int.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size.

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for setting the position.

        Args:
            value (tuple): The position, must be a tuple of 2 positive int.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #.

        Prints an empty line if size is 0.
        Prints spaces according to position before the square.
        """
        if self.__size == 0:
            print()
            return

        # Print lines before the square if position[1] > 0
        print("\n" * self.__position[1], end="")

        # Print the square with spaces for horizontal offset (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
