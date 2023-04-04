import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy module.

    Args:
    - m_a: list of lists of integers or floats, representing the first matrix
    - m_b: list of lists of integers or floats, representing the second matrix

    Returns:
    - result: list of lists of integers or floats, representing the product of the two matrices

    Raises:
    - TypeError: if m_a or m_b is not a list, or if m_a or m_b is not a list of lists, or if one element of the
                list of lists is not an integer or a float
    - ValueError: if m_a or m_b is empty, or if m_a and m_b cannot be multiplied, or if m_a or m_b is not a rectangle

    """
    # Validate input matrices
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Convert input matrices to numpy arrays
    m_a_np = np.array(m_a)
    m_b_np = np.array(m_b)

    # Perform matrix multiplication
    result_np = np.dot(m_a_np, m_b_np)

    # Convert result to list of lists
    result = result_np.tolist()

    return result
