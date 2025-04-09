# numpy_basics.py

"""
NumPy Basics: A Detailed Explanation

NumPy is a powerful numerical computing library in Python. It provides support for arrays, matrices, and many mathematical functions that operate on these data structures.
"""

# Importing NumPy
import numpy as np

# Creating Arrays
# ----------------
# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Creating arrays with initial values
zeros_array = np.zeros((2, 3))  # 2x3 array of zeros
print("Zeros Array:\n", zeros_array)

ones_array = np.ones((2, 3))  # 2x3 array of ones
print("Ones Array:\n", ones_array)

# Creating an array with a range of values
range_array = np.arange(0, 10, 2)  # Start at 0, end before 10, step by 2
print("Range Array:", range_array)

# Creating an array with evenly spaced values
linspace_array = np.linspace(0, 1, 5)  # 5 values between 0 and 1 inclusive
print("Linspace Array:", linspace_array)

# Array Operations
# ----------------
# Element-wise operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

add_array = array_a + array_b  # Element-wise addition
print("Element-wise Addition:", add_array)

multiply_array = array_a * array_b  # Element-wise multiplication
print("Element-wise Multiplication:", multiply_array)

# Matrix Operations
# -----------------
# Dot product
dot_product = np.dot(array_a, array_b)  # Dot product of two arrays
print("Dot Product:", dot_product)

# Transpose of a matrix
transpose_array = array_2d.T
print("Transpose of 2D Array:\n", transpose_array)

# Indexing and Slicing
# --------------------
# Indexing
print("Element at index 0 in 1D array:", array_1d[0])
print("Element at row 0, column 1 in 2D array:", array_2d[0, 1])

# Slicing
print("Slicing first three elements in 1D array:", array_1d[:3])
print("Slicing the first row in 2D array:\n", array_2d[0, :])

# Basic Functions
# ---------------
# Sum of all elements
sum_of_elements = np.sum(array_1d)
print("Sum of all elements in 1D array:", sum_of_elements)

# Mean of all elements
mean_of_elements = np.mean(array_1d)
print("Mean of all elements in 1D array:", mean_of_elements)

# Standard deviation of all elements
std_deviation = np.std(array_1d)
print("Standard Deviation of all elements in 1D array:", std_deviation)

# Reshaping Arrays
# ----------------
reshaped_array = array_1d.reshape((5, 1))  # Reshaping 1D array to 5x1 2D array
print("Reshaped 1D Array to 5x1 2D Array:\n", reshaped_array)

# Conclusion
# ----------
# This script covers the basic concepts of NumPy including array creation, basic operations, indexing, slicing, and some fundamental functions.
# NumPy is an essential library for scientific computing and provides a foundation for more advanced libraries like SciPy and Pandas.
