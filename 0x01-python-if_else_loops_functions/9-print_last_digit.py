#!/usr/bin/python3

def print_last_digit(number):

    lastNum = abs(number) % 10
    print("{}".format(lastNum), end="")
    return lastNum
