#!/usr/bin/python3
"""task 12 pascal"""


def pascal_triangle(n):
    """Pascal triangle."""
    row = []
    for num in range(n):
        x = 11**num
        row.append(str(x))
    return row
