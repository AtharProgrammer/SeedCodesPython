'''
Array Attributes
NumPy arrays have several attributes that you can access
'''
import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Create a 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr2d.shape)    #(2,3)
print(arr2d.ndim)     # 2
print(arr3d.size)     # 8
print(arr1d.dtype)    # int32


