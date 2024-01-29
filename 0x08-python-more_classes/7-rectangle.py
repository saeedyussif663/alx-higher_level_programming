#!/usr/bin/python3
"""Private instance attribute: width and height
Instantiation with height and width
Public class attribute: number_of_instances
public method: area (returns the area of the rectangle)
     parameter (returns the parameter of the rectangle)
__str__: prints the character #
__repr__:  return a string representation of the rectangle to be \
able to recreate a new instance by using eval()
Print the message Bye rectangle... if an instance is deleted
"""


class Rectangle:
    """defines a rectangle based on 5-rectangle.py"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        message = ""
        for _ in range(self.__height):
            message += str(self.print_symbol) * self.__width
            if _ != self.__height - 1:
                message += "\n"
        return message

    def __repr__(self):
        return f"{self.__class__.__name__}{(self.__width, self.__height)}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
