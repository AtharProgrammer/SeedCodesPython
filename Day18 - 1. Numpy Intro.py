'''
What is NumPy?
NumPy is a Python library used for numerical computing. It provides support for arrays, matrices, and mathematical functions to
operate on these arrays.NumPy is widely used in scientific and numerical computing because of its efficiency and ease of use.

Installation
If you haven't installed NumPy yet, you can install it using pip, the Python package manager

pip install numpy

Importing NumPy
To use NumPy in your Python script or interactive session, you need to import it:

import numpy as np


Basics of NumPy Arrays
NumPy's main object is the ndarray (n-dimensional array). It is a table of elements (usually numbers),
all of the same type, indexed by a tuple of non-negative integers. Here's how you can create a NumPy array:
'''

import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)
# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
# Create a 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)
