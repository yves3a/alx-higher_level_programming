#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after . ? and :
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after . ? and :
    Args:
        text: text to print
    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Print the text with 2 new lines after . ? and :
    for char in text:
        if char in ".?:":
            print("\n")
        else:
            print(char, end="")
