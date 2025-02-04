#!/usr/bin/python3
"""Module for append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file
        search_string (str): The string to search for in each line
        new_string (str): The string to insert after matching lines
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
