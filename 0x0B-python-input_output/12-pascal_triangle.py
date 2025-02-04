#!/usr/bin/python3
"""Module for pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle to generate

    Returns:
        list: Empty list if n <= 0, otherwise the Pascal's
        triangle as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # First number in row is always 1
        prev_row = triangle[i - 1]

        # Calculate middle numbers in the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Last number in row is always 1
        triangle.append(row)

    return triangle
