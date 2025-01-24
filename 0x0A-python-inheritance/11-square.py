#!/usr/bin/python3
"""
A module that represents Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class that inherits from the Rectangle """
    
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def __str__(self):
        """ Returning string representation of the square """
        return f"[Square] {self.__size}/{self.__size}"