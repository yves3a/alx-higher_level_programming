#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []

    # iterating through each row
    for row in matrix:
        # creating a new row
        new_row = []
        for i in row:
            new_row.append(i**2)
        new_matrix.append(new_row)
    return new_matrix
