#!/usr/bin/python3
""" class base """


Rectangle = __import__('9-rectangle').Rectangle


""" Square class """


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size init"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        size_str = str(self.__size)
        max_size_str_length = 245 - len("[Square] ") - 1  # Account for the "[Square] " prefix and the slash in the output
        if len(size_str) > max_size_str_length:
            size_str = size_str[:max_size_str_length]
        return "[Square] " + size_str + "/" + size_str
