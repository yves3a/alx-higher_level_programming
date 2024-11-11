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

    text = text.strip()
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="")
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
