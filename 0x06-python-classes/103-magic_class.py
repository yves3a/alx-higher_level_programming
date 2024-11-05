#!/usr/bin/python3
"""Module that defines a MagicClass"""
import math


class MagicClass:
    """A class that defines a circle"""

    def __init__(self, radius=0):
        """Initialize the MagicClass instance.

        Args:
            radius (number): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle"""
        return 2 * math.pi * self.__radius
