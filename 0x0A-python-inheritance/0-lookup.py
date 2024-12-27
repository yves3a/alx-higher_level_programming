#!/usr/bin/python3
""" Representing a function that lists available attributes and methods """


def lookup(obj):
    """ Returns a list of available attributes and methods of an objects """
    return dir(obj)
