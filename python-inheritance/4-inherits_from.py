#!/usr/bin/python3
"""task 4"""


def inherits_from(obj, a_class):
    """return"""
    if type(obj) == a_class:
        return False

    return issubclass(type(obj), a_class)
