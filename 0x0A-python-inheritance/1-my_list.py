#!/usr/bin/python3
"""The my_list module contains MyList class
"""


class MyList(list):
    """DeviredClassName from list
    Public instance method: def print_sorted(self): \
    that prints the list, but sorted (ascending sort)
    """
    def __init__(self):
        "initializing the inheritance"
        super().__init__()

    def print_sorted(self):
        """returns new sorted list"""
        lst = self.copy()
        lst.sort()
        print(lst)
