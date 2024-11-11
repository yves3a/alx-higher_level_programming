#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix: List of lists containing integers or floats
        div: Number to divide matrix elements by

    Returns:
        New matrix with elements divided by div

    Raises:
        TypeError: If matrix is not list of lists of integers/floats,
                  If rows are not same size,
                  If div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float))
              for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]