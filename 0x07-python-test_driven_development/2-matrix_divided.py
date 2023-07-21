#!/usr/bin/python3
""" Provides matrix functions"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
            Each row must be of the same size and contain integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by the divisor and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats, or if each row has different sizes.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round each element to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
