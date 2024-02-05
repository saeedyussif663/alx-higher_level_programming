#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry \
(7-base_geometry.py). (task based on 8-rectangle.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle Class"""

    def __init__(self, width, height):
        """Initializes the class

        Args:
        - width: Width of the figure
        - height: Height of the figure
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
