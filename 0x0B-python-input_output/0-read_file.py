#!/usr/bin/python3
"""
Provides functions for reading and printing the contents of a text file.

Author: Ian Mburu
"""


def read_file(filename=""):
    """
    Read the contents of a text file and print them to stdout.

    Args:
        filename (str): Name of the text file to be read.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.

    Example:
        read_file("example.txt")
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
