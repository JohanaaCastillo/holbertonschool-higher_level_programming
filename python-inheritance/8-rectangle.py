#!/usr/bin/python3
"""basegeometryclass"""


class Rectangle(BaseGeometry):
    """This is a class Rectangle"""

    def __init__(self, width, height):
        """This is a Constructor.
        Args:
            width: of Rectangle
            height: of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height