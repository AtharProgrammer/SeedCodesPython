import numpy as np
# Saving and loading arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
np.save('array.npy', arr)  # Save array to a binary file
loaded_arr = np.load('array.npy')  # Load array from file
print(loaded_arr)
