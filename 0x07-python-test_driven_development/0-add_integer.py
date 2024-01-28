#!/usr/bin/python3
"""The Module contains the add integer function
the function takes two integer/float arguments a and b
b has a optional argument of 98
A TypeError is raised if either a or b is not an interger or float
Returns the sum (integer) of both arguments"""


def add_integer(a, b=98):
    """A function that returns the sum of two arguments
Args: a and b(optional_argument)to 98
Return: integer (a + b)"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        if isinstance(a, float):
            a = int(a)
        elif isinstance(b, float):
            b = int(b)
        return a + b
