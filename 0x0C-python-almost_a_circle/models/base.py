#!/usr/bin/python3
"""
This module contains the base class for the almost a circle project.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return json representation of a list if dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
