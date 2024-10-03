#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    # copying a dictionary
    new_dic = a_dictionary.copy()

    # Identifying keys to delete
    keys_to_delete = [key for key in a_dictionary if a_dictionary[key] == value]

    # iterate within keys to  delete while deleting
    for memb in keys_to_delete:
        del new_dic[memb]
    return new_dic
