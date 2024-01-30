#!/usr/bin/python3
"""Defines locked class
"""


class LockedClass:
    """Prevents the user from initialising a new class
    """
    __slots__ = ["first_name"]
