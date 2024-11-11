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
    
    i = 0
    while i < len(text):
        # Skip spaces at the beginning of the text
        if text[i] == " " and i == 0:
            i += 1
            continue
        # Skip spaces after . ? and :
        if i > 0 and text[i] == " " and text[i - 1] in ".?:":
            i += 1
            continue
        
        #
        print(text[i], end="")

        # Print 2 new lines after . ? and : 
        if text[i] in ".?:":
            print("\n")
        i += 1
