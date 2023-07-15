#!/usr/bin/python3
"""
Provides functions for returning an object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string representing the object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
