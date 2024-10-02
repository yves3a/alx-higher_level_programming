#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for memb in a_dictionary:
        if memb == key:
            del a_dictionary[key]
        return a_dictionary
