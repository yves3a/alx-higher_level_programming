#!/usr/bin/python3
"""
A module that  represents a square class that inherits from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ A square that inherits from Rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
