#!/usr/bin/python3
"""This is a module for square"""


class Square():
    """
    Creates a square class object
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ Gets size of square"""
        return self.__size

    @size.setter
    def __init__(self, value):
        """
        Initializes instance of a square
        Arguments:
            size
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns area of square based on size
        """
        return (self.__size*self.__size)

    def my_print(self):
        if (self.size):
            for x in range(self.size):
                print("#" * self.size, end='')
                print()
        else:
            print()
