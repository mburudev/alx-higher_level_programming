#!/usr/bin/python3
"""
Provides a function that returns the dictionary description.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to be retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
