#!/usr/bin/python3
"""The modules reads a file
"""


def read_file(filename=""):
    """reads the contents of a fils

    Args:
        filename(optional parameter)

    Returns: the content of the file as a string
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
