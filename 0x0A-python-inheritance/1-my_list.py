#!/usr/bin/python3
"""Provides fucntions to prints"""


class MyList(list):
    """Represents a MyList class"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
