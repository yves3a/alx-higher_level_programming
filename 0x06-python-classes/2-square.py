#!/usr/bin/python3
"""
Module 2-square
Defines a Square class with a private instance attribute size.
"""


class Square:
    """Creating a class"""

    def __init__(self, size=0):
        """
        Initialises the square with a private size attrivutes,

        Args:
        size(int): the size of it's side should be an integer

        Raises:
        TypeError: if the size is not an integer.
        ValueError: is the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
