#!/usr/bin/python3
def element_at(my_list, idx):

    # If idx is negative, return "None"
    if idx < 0:
        return "None"

    # If idx is out of range of the list, return "None"
    elif idx not in range(len(my_list)):
        return "None"

    # Otherwise, return the element at the given index
    else:
        return my_list[idx]
