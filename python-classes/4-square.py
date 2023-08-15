#!/usr/bin/python3
"""This is a module for square"""


class Square:
    """
    Creates a square class object
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ These are a getter and setter when to get
        the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Initializes instance of a square
        Arguments:
            size
        """
        if (not type(value) is int):
            raise TypeError("size must be an integer")
        if (ValueError < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns area of square based on size
        """
        return (self.__size * self.__size)
