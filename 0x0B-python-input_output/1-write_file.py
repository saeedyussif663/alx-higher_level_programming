#!/usr/bin/python3
"""the module writes to a file
"""


def write_file(filename="", text=""):
    """Writes to a file

    Args:
        filename(optional) the file to write to
        text(optional) the text to write to the file

    Returns: the number of characters
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        characters = file.write(text)

    return characters
