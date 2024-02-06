#!/usr/bin/python3
"""returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args: my_obj - the object to serialize

    Returns: JSON representation of my_obj
    """
    try:
        serialize = json.dumps(my_obj)
    except TypeError:
        raise TypeError(f"{my_obj} is not JSON serializable")
    return serialize
