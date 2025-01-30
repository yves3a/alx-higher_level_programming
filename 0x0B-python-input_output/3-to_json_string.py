#!/usr/bin/python3
""" Module for converting JSON string """
import json


def to_json_string(my_obj):
    """
    Returns a json representation of an object (string)

    Args:
        my_obj: object to be represented in json

    Returns:
        str: JSON representation of object.
    """
    return json.dumps(my_obj)
