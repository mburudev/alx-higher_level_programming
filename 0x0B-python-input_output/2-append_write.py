#!/usr/bin/python3
"""
This module provodes functions for appending to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.

    Args:
        filename (str): The name of the file to append.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
