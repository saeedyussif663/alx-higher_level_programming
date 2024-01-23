#!/usr/bin/python3

class Square:
    """Defines a square based on 3-square.py"""
    def __init__(self, size=0):
        """initializes the size attribute or set it to 0 if no value is passed
        
        Args:
            size(int): the size of the integer
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """getter for the size attribute
        
        Returns:
            int: The size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """setter function: sets the size to the value attribute
        
        Args:
            value(int): The new_size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """a public method that calculates the area of the square
        
        Returns:
            int: The area of the square
        """
        return self.__size * self.__size
