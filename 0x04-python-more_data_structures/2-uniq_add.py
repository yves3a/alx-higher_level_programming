#!/usr/bin/python3
def uniq_add(my_list=[]):
    # removing any duplicate from the list
    new_list = set(my_list)
    Sum = 0
    for num in new_list:
        Sum += num
    return Sum
