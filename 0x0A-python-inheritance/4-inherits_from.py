#!/usr/bin/python3
""" The module contains inherits func
the function  returns True if the object is an instance of a class \
that inherited (directly or indirectly) \
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Returns  returns True if the object is an instance of \
    a class that inherited (directly or indirectly) from the \
    specified class ; otherwise False.
    Args:
        obj: object to check
        a_class: class to be checked against
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
