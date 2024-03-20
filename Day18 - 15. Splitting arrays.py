import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

splitted_array = np.split(arr, 2, axis=1)  # Split along columns
print(splitted_array)

'''
[array([[1, 2],
       [5, 6]]), array([[3, 4],
       [7, 8]])]'
