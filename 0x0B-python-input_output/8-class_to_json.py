#!/usr/bin/python3
"""
Provides a function that returns the dictionary description.
"""
import json


def class_to_json(obj):
    """
    Returns a dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object.

    Example:
        class MyClass:
            def __init__(self, name, age, is_active):
                self.name = name
                self.age = age
                self.is_active = is_active

        obj = MyClass("John", 25, True)
        json_dict = class_to_json(obj)
        print(json_dict)
    """
    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
