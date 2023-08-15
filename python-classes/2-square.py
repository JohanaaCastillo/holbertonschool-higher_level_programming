#!/usr/bin/python3
"""This is a module for square"""


class Square:
    """
    Creates a square class object
    """
    def __init__(self, size=0):
        """
        Initializes instance of a square
        Arguments:
            size
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >=0")
        self.__size = size
