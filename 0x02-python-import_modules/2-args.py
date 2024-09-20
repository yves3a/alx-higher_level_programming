#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # list of arg excluding script name
    a = len(argv)

    if a == 0:
        print("{} arguments.".format(a))
    elif a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))

    for i in range(1, a + 1):
        print("{}: {}".format(i, sys.argv[i]))
