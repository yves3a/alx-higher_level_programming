#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div."""
    msg = ("matrix must be a matrix (list of lists) "
           "of integers/floats")
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError(msg)

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError(msg)

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
