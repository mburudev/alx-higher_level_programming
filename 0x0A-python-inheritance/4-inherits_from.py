#!/usr/bin/python3
"""Provides inherits_from function"""


def inherits_from(obj, a_class):
    """
    the object is an instance of a class that inherited
    obj: an object
    a_class: a class
    returns None
    """
    return type(obj) != a_class and isinstance(obj, a_class)
