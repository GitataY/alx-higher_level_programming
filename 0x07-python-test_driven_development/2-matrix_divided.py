#!/usr/bin/python3
""""This module divides all elements of the matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix represented as a list
        of lists of integers or floats.
        div (int or float): Divisor to divide the matrix elements.

    Returns:
        list of lists: A new matrix with elements divided by the
            divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) 
     for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)
             of integers/floats")

    # Check if each row of the matrix has the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
