#!/usr/bin/python3
"""
This module contains the base class for the almost a circle project.
"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of json string representation
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
            **dictionary: Double pointer to a dictionary of attributes
        Returns:
            An instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create dummy Rectangle with width=1, height=1
        elif cls.__name__ == "Square":
            dummy = cls(1)     # Create dummy Square with size=1

        # Update the dummy instance with real values
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file
        Returns:
            If the file doesn't exist - an empty list
            Otherwise - a list of instances
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to CSV file
        """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes CSV file to list of instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                instances = []
                for row in reader:
                    row = [int(x) for x in row]  # Convert strings to integers
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            'id': row[0],
                            'width': row[1],
                            'height': row[2],
                            'x': row[3],
                            'y': row[4]
                        }
                    elif cls.__name__ == "Square":
                        dictionary = {
                            'id': row[0],
                            'size': row[1],
                            'x': row[2],
                            'y': row[3]
                        }
                    instance = cls.create(**dictionary)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
