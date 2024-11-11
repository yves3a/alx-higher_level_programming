#!/usr/bin/python3
""" Module that prints a square """


def print_square(size):
    """ Function that prints a square """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
