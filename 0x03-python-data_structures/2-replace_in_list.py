#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    # is idx is negative, do nothing.
    if idx < 0:
        return my_list

    # if idx is out of a range. just return orginal one
    elif idx not in range(len(my_list)):
        return my_list

    # otherwise should replace an element
    else:
        my_list[idx] = element
        return my_list
