#!/usr/bin/python3
"""created task 4"""


def print_square(size):
    """Prints square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for _ in range(0, size):
            print("#", end="")
        print()
