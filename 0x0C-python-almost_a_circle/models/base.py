#!/usr/bin/python3
"""
This module contains the base class for the almost a circle project.
"""


class Base:
    """this is the base class for the almost a circle project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects