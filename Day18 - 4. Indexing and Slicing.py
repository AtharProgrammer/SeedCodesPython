'''
Indexing and Slicing
You can access elements, rows, columns, or subarrays of a NumPy array
using indexing and slicing
'''

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[0])        # First row[1 2 3]
print(arr[:, 0])     # First column[1 4 7]
print(arr[1:2, :3])  # Subarray[[4 5 6]]





