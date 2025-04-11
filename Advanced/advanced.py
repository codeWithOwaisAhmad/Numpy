"""
NumPy Advanced Level Tutorial
==============================

This tutorial covers advanced-level NumPy concepts including advanced indexing,
broadcasting tricks, structured arrays, and more complex linear algebra operations.

Author: codeWithOwaisAhmad
Date: 2025-02-05
"""

import numpy as np

# 1. Advanced Indexing
# ---------------------

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array:")
print(array_2d)

# Boolean indexing
bool_index = array_2d > 5
print("\nBoolean indexing (elements > 5):")
print(bool_index)
print(array_2d[bool_index])

# Fancy indexing
fancy_index = array_2d[[0, 1, 2], [0, 1, 2]]
print("\nFancy indexing (diagonal elements):")
print(fancy_index)

# 2. Broadcasting Tricks
# -----------------------

# Create two arrays of different shapes
array_a = np.array([1, 2, 3])
array_b = np.array([[1], [2], [3]])

# Broadcasting to perform element-wise multiplication
broadcasted_product = array_a * array_b
print("\nBroadcasted product:")
print(broadcasted_product)

# 3. Structured Arrays
# ---------------------

# Create a structured array
structured_array = np.array([(1, 'Alice', 25), (2, 'Bob', 30)],
                            dtype=[('id', 'i4'), ('name', 'U10'), ('age', 'i4')])
print("\nStructured array:")
print(structured_array)

# Accessing fields
print("\nNames in structured array:")
print(structured_array['name'])

# 4. More Complex Linear Algebra Operations
# ------------------------------------------

# Create a matrix
matrix_c = np.array([[2, 1], [1, 2]])

# Singular Value Decomposition (SVD)
U, S, V = np.linalg.svd(matrix_c)
print("\nSingular Value Decomposition (SVD):")
print("U matrix:")
print(U)
print("Singular values:")
print(S)
print("V matrix:")
print(V)

# Solving a system of linear equations
# Example: Solve 2x + y = 1 and x + 2y = 1
A = np.array([[2, 1], [1, 2]])
b = np.array([1, 1])
solution = np.linalg.solve(A, b)
print("\nSolution to the system of linear equations:")
print(solution)

# Eigenvalues and eigenvectors of a non-square matrix using the SVD
U, S, V = np.linalg.svd(matrix_c, full_matrices=False)
eigenvalues = S
print("\nEigenvalues of the non-square matrix using SVD:")
print(eigenvalues)

# This concludes the advanced-level NumPy tutorial.
