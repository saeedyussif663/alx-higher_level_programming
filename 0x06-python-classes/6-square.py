#!/usr/bin/python3
class Square:
    """defines a square based on 5-square.py"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a square

        Args:
            size (int, optional): The size of the square,
                    Defaults to 0
            position (tuple, optional): The position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter for the size attribute

        Returns:
        int: the size of the square
        """
        return self.__size

    @property
    def position(self):
        """getter for the position attribute

        Returns:
            tuple:the position of the square
        """
        return self.__position

    @size.setter
    def size(self, value):
        """setter function: sets the size to the value attribute

        Args:
            value(int): The value for a side of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter function: sets the size to the position attribute

        Args:
            value(tuple): The position of the square
        """
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def area(self):
        """public instance method that rcalculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size
