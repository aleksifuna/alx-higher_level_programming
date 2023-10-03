#!/usr/bin/python3
"""
This module contains one function matrix_divided
"""


def matrix_divided(matrix, div):
    """computes the quotient of each element in a matrix by a integer or float
    and returns a new matrix of the quotients.

    Args:
        matrix: list of integers or floats dividend
        div: integer or float representing the divisor

    Returns:
        a new matrix of the quotients

    Raises:
        TypeError: if an element in the matrix is not int or float
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is zero

        """
    m = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(m)
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
