#!/usr/bin/python3
"""Module for returning a description of an object for a json serialization"""
import json


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization
    Args:
        obj: instance of a Class
    Returns:
        dictionary representation of the object
    """
    return obj.__dict__
