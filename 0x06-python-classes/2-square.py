#!/usr/bin/python3

class Square:
    """Defines a square based on 1-square.py"""
    def __init__(self, size=0):
        """initializes the size attribute or set it to 0 if no value is passed
        
        Args:
            value(int): The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
