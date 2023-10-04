#!/usr/bin/python3
import numpy as np
"""This module supplies a function lazy_matrix_mul
"""


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrices and returns the multiple

    Args:
        m_a: a list of lists representing matrix a
        m_b: a list of lists representing matric b

    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a list of lists
        ValueError: if m_a or m_b is empty
        TypeError: if one of the elements in the list is not an integer
        TypeError: if lists in list are not of same size
        ValueError: if m_a and m_b cant be multiplied
    Return: product matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    if type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    for row in m_a:
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_a)):
        if len(m_a[0]) != len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        if len(m_b[0]) != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")
    rows_mb = len(m_b)
    rows_ma = len(m_a)
    cols_mb = len(m_b[0])
    cols_ma = len(m_a[0])

    if cols_ma != rows_mb:
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.matmul(m_a, m_b).tolist()

    return result
