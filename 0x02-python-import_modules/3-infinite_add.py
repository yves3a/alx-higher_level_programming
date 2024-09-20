#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    result = 0

    # loop through each argument and convert it into an interger.
    for i in argv:
        result += int(i)

    # print the final result
    print("{}".format(result))
