#!/usr/bin/python3
"""Provides a locked class."""


class LockedClass:
    """
    Prevents the user from instantiating a new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
