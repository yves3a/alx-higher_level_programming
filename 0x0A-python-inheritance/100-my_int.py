#!/usr/bin/python3
"""
A module represents a class that inherits form int
"""


class MyInt(int):
    """ A class that inherits from int with inverted == and != operators """

    def __eq__(self, other):
        """Override equals operator"""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """Override not equals operator"""
        return super().__eq__(other)
