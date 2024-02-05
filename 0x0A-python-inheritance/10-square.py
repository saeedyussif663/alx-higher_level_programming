#!/usr/bin/python3
"""class Square that inherits from Rectangle \
(9-rectangle.py). (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square Class"""

    def __init__(self, size):
        """Initializes the class
        """

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        "returns the string representation"
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        "returns the area of the square"
        return self.__size * self.__size
