#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()  # Print a blank line for empty row
        else:
            for i in range(len(row)):
                if i != len(row) - 1:
                    print("{:d}".format(row[i]), end=" ")
                else:
                    print("{:d}".format(row[i]), end="")
            print()  # Move to the next line after each row

