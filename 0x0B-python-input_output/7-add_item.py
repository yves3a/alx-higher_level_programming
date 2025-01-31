#!/usr/bin/python3
"""Module for adding all argument to python list and save them"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Trying to load an existing file or create an empty list
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

# Adding all arguments to the list (excluding script name)
my_list.extend(sys.argv[1:])

# Save the updated list to a file
save_to_json_file(my_list, "add_item.json")
