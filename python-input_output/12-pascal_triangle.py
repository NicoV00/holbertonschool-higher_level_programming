#!/usr/bin/python3
"""task 12 pascal"""


def pascal_triangle(n):
    """pascal triangle"""
    row = []
    for i in range(n):
        current_row = [1] * (i + 1)
        row.append(current_row)
    return row
