#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return "None"
    # initialise max_value to be the first element
    max_num = my_list[0]
    # Loopint through each number of list
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num
