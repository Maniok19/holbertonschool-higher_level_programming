#!/usr/bin/python3
"""Module that divides all elements of a matrix
description
    matrix_divided(matrix, div)"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    Args:
        matrix: list of lists of integers or floats
        div: integer or float
    Returns:
        new matrix"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]
