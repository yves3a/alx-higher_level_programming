#!/usr/bin/python3
"""Module that appends a text into a file"""


def append_write(filename="", text=""):
    """
    Appends a text at the end of a text file

    Args:
        filename(str): file to be appended into
        text(str): a text to be appended

    Returns:
        int: number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
