'''
Matrix Operations: Perform operations such as addition, multiplication, and transpose on matrices represented as lists of lists.
'''

# Matrix addition
def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

# Example
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_addition(matrix1, matrix2)
print(result)  # Output: [[6, 8], [10, 12]]

# Matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

# Example
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_multiplication(matrix1, matrix2)
print(result)  # Output: [[19, 22], [43, 50]]

# Matrix transpose
def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Example
matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = matrix_transpose(matrix)
print(transposed_matrix)  # Output: [[1, 4], [2, 5], [3, 6]]
