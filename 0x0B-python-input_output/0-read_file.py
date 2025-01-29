#!/usr/bin/python3
"""
A module of function that reads a text and prints it to stdout
"""


def read_file(filename=""):
    """ A funtion that reads text file and prints it to stdout """

    with open(filename, mode="r", encoding="utf-8") as myfile:
        for line in myfile:
            print(line, end="")
    print()
