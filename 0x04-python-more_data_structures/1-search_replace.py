#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index = 0
    # iterating through each element from the list
    for num in my_list:
        if num == search:
            my_list[index] = replace
        index += 1
    return my_list
