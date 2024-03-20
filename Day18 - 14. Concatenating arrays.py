import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

concatenated_array = np.concatenate((arr1, arr2), axis=0)  # Concatenate along rows
print(concatenated_array)

'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
 '''
