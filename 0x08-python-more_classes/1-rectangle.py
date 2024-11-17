#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise a new Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieving the width"""

        return self.__width
    
    @width.setter
    def width(self, value):
        """ Setting the width value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value
    
    @property
    def height(self):
        """Retrieving the height"""

        return self.__width
    
    @height.setter
    def height(self, value):
        """Setting the height value"""
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
