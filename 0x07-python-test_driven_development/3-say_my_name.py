#!/usr/bin/python3
""" The module contains a function that prints full name
raises a TypeError if either first_name or last_name is not a string
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>
    Args: first_name (string)
    last_name (string)
    Return: My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("first_name must be a string")
    print(f"My name is {first_name} {last_name}")
