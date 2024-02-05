#!/usr/bin/python3
"""BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """BaseGeometry (based on 5-base_geometry.py)
    Public instance method: def area(self): that raises an Exception \
    with the message area() is not implemented
    """
    def __init__(self):
        "init function"
        pass

    def area(self):
        "raises an exception"
        raise Exception("area() is not implemented")
