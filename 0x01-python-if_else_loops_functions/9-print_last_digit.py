#!/usr/bin/python
def print_last_digit(number):

    lastNum = abs(number % 10)
    print("{}".format(lastNum))
    return lastNum
