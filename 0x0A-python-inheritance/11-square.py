#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)\
(task based on 10-square.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle (9-rectangle.py). (\
    task based on 10-square.py)."""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns string representation of the object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
