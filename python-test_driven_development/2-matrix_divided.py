#!/usr/bin/python3
"""Created task 2"""


def matrix_divided(matrix, div):
    """Divides the matrix."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or not
        all(isinstance(elem, list) for elem in matrix)):
        raise TypeError(msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    new_list = []
    len_row = len(matrix[0])
    for elem in matrix:
        if len_row != len(elem):
            raise TypeError("Each row of the matrix must have the same size")
        for num in elem:
            if isinstance(num, (int, float)):
                new_list.append(round(num / div, 2))
            else:
                raise TypeError(msg)
        new_matrix.append(new_list)
        new_list = []

    return new_matrix
