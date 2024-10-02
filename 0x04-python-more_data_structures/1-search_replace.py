#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index = 0
    new_list = my_list.copy()
    # iterating through each element from the list
    for num in new_list:
        if num == search:
            new_list[index] = replace
        index += 1
    return new_list
