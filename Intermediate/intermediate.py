"""
NumPy Intermediate Level Tutorial
==================================

This tutorial covers intermediate-level NumPy concepts including array manipulation,
broadcasting, and basic linear algebra operations.

Author: codeWithOwaisAhmad
Date: 2025-02-05
"""

import numpy as np

# 1. Array Manipulation
# ---------------------

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D array:")
print(array_2d)

# Reshape an array
reshaped_array = array_2d.reshape(3, 2)
print("\nReshaped array (3x2):")
print(reshaped_array)

# Flatten an array
flattened_array = array_2d.flatten()
print("\nFlattened array:")
print(flattened_array)

# Transpose an array
transposed_array = array_2d.T
print("\nTransposed array:")
print(transposed_array)

# 2. Broadcasting
# ---------------

# Broadcasting allows NumPy to perform element-wise operations on arrays of different shapes
array1 = np.array([1, 2, 3])
array2 = np.array([[1], [2], [3]])

# Adding a 1D array to a 2D array
broadcasted_sum = array1 + array2
print("\nBroadcasted sum:")
print(broadcasted_sum)

# 3. Basic Linear Algebra Operations
# ----------------------------------

# Create two matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("\nMatrix product:")
print(matrix_product)

# Element-wise multiplication
elementwise_product = matrix_a * matrix_b
print("\nElement-wise product:")
print(elementwise_product)

# Determinant of a matrix
determinant = np.linalg.det(matrix_a)
print("\nDeterminant of matrix_a:")
print(determinant)

# Inverse of a matrix
inverse_matrix = np.linalg.inv(matrix_a)
print("\nInverse of matrix_a:")
print(inverse_matrix)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix_a)
print("\nEigenvalues of matrix_a:")
print(eigenvalues)
print("\nEigenvectors of matrix_a:")
print(eigenvectors)

# This concludes the intermediate-level NumPy tutorial.