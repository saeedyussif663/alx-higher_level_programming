#!/usr/bin/python3
""" The module contains the is_kind_class func
the function  returns True if the  instance of, or if the object is an \
instance of a class  that inherited from, the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Returns true if an object is  instance of, or if the\
    object is an instance of a class that inherited from, the \
    specified class ; otherwise False
    Args:
        obj: object to check
        a_class: class to be checked against
    """
    return isinstance(obj, a_class)
