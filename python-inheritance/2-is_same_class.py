#!/usr/bin/python3
"""task 2"""


def is_same_class(obj, a_class):
    """return"""
    if type(obj) is type(a_class):
        return True
    else:
        return False
