#!/usr/bin/python3
"""
This module provides functions for returning the pascals triangle.
"""


def pascal_triangle(n):
    """
    Provides a list if intergers representing pascals triangle.

    Args:
        n (int): the interges whose pascals triangle is to be printed

    Returns:
        list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[-1]
        current_row = [1]

        for j in range(1, i):
            current_element = previous_row[j - 1] + previous_row[j]
            current_row.append(current_element)

        current_row.append(1)
        triangle.append(current_row)

    return triangle
