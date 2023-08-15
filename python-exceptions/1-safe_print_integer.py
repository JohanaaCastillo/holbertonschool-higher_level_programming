#!/usr/bin/python3
def safe_list_integers(value):
    try:
        print("{:d}".format(value), end='')
        return True
    except (ValueError, TypeError):
        pass
        return False
