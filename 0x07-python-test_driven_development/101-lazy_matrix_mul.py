#!/usr/bin/python3
"""Lazy matrix multiplication"""


import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using the NumPy module."""

    np_a = np.array(m_a)
    np_b = np.array(m_b)

    try:
        result = np.dot(np_a, np_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
