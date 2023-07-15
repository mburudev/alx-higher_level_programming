#!/usr/bin/python3
"""
Provides a that writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write.

    Returns:
        None
    """
    try:
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
    except TypeError:
        print("An error occurred while serializing the object.")
