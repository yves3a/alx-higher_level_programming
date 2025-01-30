#!/usr/bin/python3
"""Module for creating a object"""
import json


def load_from_json_file(filename):
    """
    Creates object from a JSON file

    Args:
        filename: a name of the file 
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
