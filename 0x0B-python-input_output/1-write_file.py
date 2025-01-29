#!/usr/bin/python3
"""Module that contains write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns
    number of characters written

    Args:
        filename (str): name of the file to write to
        text (str): text to write to the file

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
