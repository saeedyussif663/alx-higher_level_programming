#!/usr/bin/python3

class Square:
    """Defines a square based on 2-square.py"""
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

    def area(self):
        """a public method that calculates the area of the square
        
        Returns:
            int: The area of the square
        """
        return self.__size * self.__size
