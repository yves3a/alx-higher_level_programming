#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new_list = my_list.copy()
        if idx < 0:
            return new_list

        elif idx not in range(len(my_list)):
            return new_list
        else:
            new_list[idx] = element
            return new_list
