#!/usr/bin/python3
"""Module for add_integer
"""


def add_integer(a, b=98):
    """Function to add two integers.

    Args:
        a (int, float): is a number.
        b (int, float): is number to add to a.

    Returns:
        int: The value of a add b. or Error message if
        a or b is not integer or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b
