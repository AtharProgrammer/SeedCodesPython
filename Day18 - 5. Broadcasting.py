import numpy as np
'''
Broadcasting
NumPy arrays support broadcasting, which allows arithmetic operations
between arrays with different shapes
'''
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2

print(arr + scalar)  # Broadcasting scalar to array

'''
[[3 4 5]
 [6 7 8]]
 '''
