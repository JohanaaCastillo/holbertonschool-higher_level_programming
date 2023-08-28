The ``0-add_integer`` module
======================

Using ``add_integer``
-------------------

This test text file in for function add_integer.  First import
``add_integer`` from the ``0-add_integer`` module:

    >>> add_integer = __import__('0-add_integer').add_integer

Now use it:

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(4, -500.2)
    -496
    >>> add_integer(4, None)
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    >>> add_integer()
    Traceback (most recent call last):
    ...
    TypeError: add_integer() missing 1 required positional argument: 'a'