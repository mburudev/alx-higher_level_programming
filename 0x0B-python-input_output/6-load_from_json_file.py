#!/usr/bin/python3
"""
Provides functions that create an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name or path of the JSON file.

    Returns:
        object: The Python object created from the JSON file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        JSONDecodeError: If the contents of the file cannot be parsed as JSON.

    Example:
        filename = 'data.json'
        obj = load_from_json_file(filename)
        print(obj)
    """
    with open(filename, 'r') as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
