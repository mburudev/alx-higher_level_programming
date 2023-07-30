#!/usr/bin/python3
"""
more class base
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be greater than 0")
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.width, self.height)
