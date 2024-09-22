#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul
    import sys

    # Check if the right number of arguments were passed
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    i = int(sys.argv[1])  # First number
    z = sys.argv[2]       # Operator
    j = int(sys.argv[3])  # Second number

    # Check if the operator is valid
    if z not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # Perform the operation based on the operator
    if z == '+':
        print("{} + {} = {}".format(i, j, add(i, j)))
    elif z == '-':
        print("{} - {} = {}".format(i, j, sub(i, j)))
    elif z == '*':
        print("{} * {} = {}".format(i, j, mul(i, j)))
    elif z == '/':
        print("{} / {} = {}".format(i, j, div(i, j)))
