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
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the json string representation of the list of objects to a file.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        
        # Convert objects to dictionaries first
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))
