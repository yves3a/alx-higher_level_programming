#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of class student"""
        if (type(attrs) is list and
                all(isinstance(item, str) for item in attrs)):
            return {key: getattr(self, key) for key in attrs
                      if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
