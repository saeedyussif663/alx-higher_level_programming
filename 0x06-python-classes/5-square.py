#!/usr/bin/python3
"""
Module: 4-square
Class Square that defines a square by:
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0)
- Size must be an integer, otherwise raise a TypeError
  exception with the message size must be an integer
- If size is less than 0, raise a ValueError exception with
  the message size must be >= 0
- Public instance method: def area(self) that returns the current square area
- Public instance method: def my_print(self) that prints in stdout the square
  with the character '#'
- Setter method: def size(self, value)
- Getter method: def size(self)
"""


class Square:
    """ defines a square based on 4-square.py"""
    def __init__(self, size=0):
        """initializes the size attribute or set it to 0 if no value is passed

        Args:
            size(int, optional): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """returns the size of the square

        Returns:
            int: the size of the square
        """
        return self.size

    @size.setter
    def size(self, value):
        """sets the size of the square with value

        Args:
            value(int): The value for the size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """public instance method that returns the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """public instance method that prints in stdout,
        the square with the character #

        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
