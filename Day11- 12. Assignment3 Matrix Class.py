'''
Assignment 3: Matrix Class
Description: Create a class representing matrices.
Implement methods to overload the arithmetic operators (+, -, *) for matrix
addition, subtraction, and multiplication.

Solution:
'''

class Matrix:
    def __init__(self, data):
        self.data = data
    
    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])
    
    def __sub__(self, other):
        return Matrix([[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])
    
    def __mul__(self, other):
        result = [[0 for _ in range(len(other.data[0]))] for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Test the Matrix class
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print(m1 + m2)    # Output: 6 8 \n 10 12
print(m1 - m2)    # Output: -4 -4 \n -4 -4
print(m1 * m2)    # Output: 19 22 \n 43 50
