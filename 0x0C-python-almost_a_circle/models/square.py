#!/usr/bin/python3
"""Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        "init function"
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "str function"
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        "size getter"
        return self.width

    @size.setter
    def size(self, value):
        "size setter"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        "update method"
        if len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        "to dict method"
        dict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
        return dict
