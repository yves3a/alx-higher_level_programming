#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    for i in my_list[-1:]:
        if my_list:
            for i in my_list[::-1]:
                print("{}".format(i))