#!/usr/bin/python3
"""appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8) \
    and returns the number of characters added

    Args:
        filename(optional): the filename to append
        text(optional): the text to append

    Return: the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        characters = file.write(text)
    return characters
