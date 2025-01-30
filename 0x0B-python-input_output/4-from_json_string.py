#!/usr/bin/python3
""" Module for converting from JSON string to python object"""
import json


def from_json_string(my_str):
    """
    Returns an object (python data structure) represented by JSON string

    Args:
        my_str:JSON string to converted to python object
    Returns:
        Object: python data structure
    """
    return json.loads(my_str)
