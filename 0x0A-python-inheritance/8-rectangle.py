#!/usr/bin/python3
""" class Rectangle that inherits from \
BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    Instantiation with width and height
    Args:
        - width: Width of the figure
        - height: Height of the figure
    """
    def __init__(self, width, height):
        "initializing function"
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
