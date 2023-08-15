#!/usr/bin/python3
def safe_list_integer(value):
    try:
        print("{:d}".format(value), end='')
        return True
    except (ValueError, TypeError):
        return False
