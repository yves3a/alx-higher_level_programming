#!/usr/bin/python3
""""Module for writing object to text file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """"
    It writes object to a text file using JSON representation

    Args:
        my_obj: object to be written
        filename: name of the file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
