#!/usr/bin/python3
"""
This module provides functions for writing to a text file.

Author: Ian Mburu
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file, returns the number of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w') as f:
        return f.write(text)
