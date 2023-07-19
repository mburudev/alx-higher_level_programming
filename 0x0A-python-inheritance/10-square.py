#!/usr/bin/python3
"""Provides functions for square class"""


Rectangle = __import__('9-rectangle').Rectangle


"""Class for square"""


class Square(Rectangle):
    """ Class for square"""
    def __init__(self, size):
        """ instantiation with size """
        self.__size = size
        super().__init__(self.__size, self.__size)
