#!/usr/bin/python3
"""The module contains a function that prints a square with the character #
raise a TypeError if size is not a integer
rais a ValueError if size is less than zero
"""


def print_square(size):
    """The print_square function prints a square with the character #
    Args: size(int) lenght of square
    Return: A square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
