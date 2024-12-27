#!/usr/bin/python3
""" Represents a class that inherits from a list """


class MyList(list):
    """ A class that inherits from list """

    def print_sorted(self):
        """ Print the sorted list """
        print(sorted(self))
