#!/usr/bin/python3
""" Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ matrix_divided
    return matrix
    """

    le = 0
    new_matrix = []
    msg_size_len = "Each row of the matrix must have the same size"
    msg_error = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) != list:
        raise TypeError(msg_error)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if type(i) != (list):
            raise TypeError(msg_error)
        if le == 0:
            le = len(i)
        if len(i) != le:
            raise TypeError(msg_size_len)

    for z in matrix:
        for m in z:
            if type(m) not in (int, float):
                raise TypeError(msg_error)

        my_list = list(map(lambda y: round((y / div), 2), z))
        new_matrix.append(my_list)

    return new_matrix
