#!/usr/bin/python3
"""
The matrix divided divides all element of a matrix
"""


def matrix_divided(matrix, div):
    """The function divides all elements of a matrix
    Arg: matrix (list of lists of integers or floats)
        div (a non-zero integer or float)
    Returns: new matrix
    """
    for i in matrix:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
    if type(matrix[0]) is not list or type(matrix[1]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in matrix:
        n_matrix = [round(num / div, 2) for num in i]
        new_matrix.append(n_matrix)
    return new_matrix
