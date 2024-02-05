#!/usr/bin/python3
"""BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """BaseGeometry (based on 6-base_geometry.py)
    Public instance method: def area(self): that raises an Exception \
    with the message area() is not implemented
    Public instance method: def integer_validator(self, name, value): \
        that validates value:
    """
    def __init__(self):
        "init funciton"
        pass

    def area(self):
        "raises an exception"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "validates the integer"
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
