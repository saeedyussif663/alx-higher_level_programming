#!/usr/bin/python3
"""returns an object (Python data structure) \
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) \
represented by a JSON string

    Args: my_str: string to deserialize

    Returns: returns an object (Python data structure)
    """
    try:
        deserialized = json.loads(my_str)
    except Exception as e:
        raise ValueError(e)
    return deserialized
