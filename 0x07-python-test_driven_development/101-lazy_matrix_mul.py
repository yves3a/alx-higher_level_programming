#!/usr/bin/python3
"""Module for matrix multiplication using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        The resulting matrix
    """
    return np.matmul(m_a, m_b)
