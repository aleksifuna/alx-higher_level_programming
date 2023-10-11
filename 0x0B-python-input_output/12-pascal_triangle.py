#!/usr/bin/python3
""" This module supplies one function pascal_triangle """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the pascal's
    triangle

    Args:
        n: size of the pascal's triangle

    Return: A list of lists representing the pascal's triangle or \
            empty list if n <= 0
    """
    pas_tri = []
    if n <= 0:
        return pas_tri
    pas_tri.append(list([1]))

    for i in range(1, n):
        temp = pas_tri[i - 1]
        pas_tri.append(list(temp))
        pas_tri_temp = []
        for num in pas_tri[i]:
            pas_tri_temp.append(num)
        for j in range(1, len(pas_tri[i])):
            a = pas_tri_temp[j]
            b = pas_tri_temp[j-1]
            pas_tri[i][j] = a + b
        pas_tri[i].append(1)

    return pas_tri
