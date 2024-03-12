class Matrix:
    def __init__(self, data):
        self.data = data

    # Overloading the multiplication operator
    def __mul__(self, scalar):
        return Matrix([[element * scalar for element in row] for row in self.data])

    # Overloading the string representation
    def __str__(self):
        return '\n'.join([' '.join([str(element) for element in row]) for row in self.data])

# Creating an instance of the Matrix class
m = Matrix([[1, 2], [3, 4]])

# Using the overloaded * operator
result = m * 2

print(result)
# Output:
# 2 4
# 6 8
