#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
'''
File_name: 0-rectangle.py
Created: 12-Jan-2024
Author: Aphrodis Uwineza (Aphrodis1st)
Size: Large
Project: 0x08-python-more_classes
'''

import numpy as np\


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
