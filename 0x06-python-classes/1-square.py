#!/usr/bin/python3
"""
Module: 1
Private instance attribute: size
Instantiation with size (no type/value verification
"""


class Square:
    """Defines a square based on 0-Square.py"""
    def __init__(self, size):
        """initializes the size to a private attribute size

        Args:
            size(int): the size of the square
        """
        self.__size = size
