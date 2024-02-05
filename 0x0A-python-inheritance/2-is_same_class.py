#!/usr/bin/python3
""" The module contains the is_same_class func
the function  returns True if the object is exactly \
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """Returns true if an object is exactly an instance of a class,\
    otherwise false
    Args:
        obj: object to check
        a_class: class to be checked against
    """
    return type(obj) is a_class
