#!/usr/bin/python3

def read_file(filename=""):
    """ A funtion that reads text file and prints it to stdout """

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
