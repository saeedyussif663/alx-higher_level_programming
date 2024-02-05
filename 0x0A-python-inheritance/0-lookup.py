#!/usr/bin/python3
"""the lookup module returns a list of objects of \
attributes and methods of an object"""


def lookup(obj):
    """returns a list of objects of atributes and methods"""
    return dir(obj)
