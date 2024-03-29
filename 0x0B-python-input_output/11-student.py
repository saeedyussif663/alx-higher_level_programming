#!/usr/bin/python3
"""Student that defines a student by: (based on 10-student.py)
"""


class Student:
    """Defines a student object"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student

        Args:
            first_name (str): First name of student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
