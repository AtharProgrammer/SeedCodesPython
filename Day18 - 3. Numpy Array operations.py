'''
Array Operations
You can perform various mathematical operations on NumPy arrays
'''

import numpy as np
# Element-wise operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)    #[5,7,9]
print(arr1 - arr2)    #[-3,-3,-3]
print(arr1 * arr2)    #[4,10,18]
print(arr1 / arr2)    #[0.25 0.4 0.5]

# Dot product
dot_product = np.dot(arr1, arr2)
print(dot_product)
# 32
