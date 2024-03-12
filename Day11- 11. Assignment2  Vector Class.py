'''
Assignment 2: Vector Class
Description: Implement a class representing 2D or 3D vectors.
Overload the arithmetic operators (+, -, *) to perform vector addition,
subtraction, and scalar multiplication.

Solution:

'''
class Vector:
    def __init__(self, *components):
        self.components = components
    
    def __add__(self, other):
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        return Vector(*[a - b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, scalar):
        return Vector(*[a * scalar for a in self.components])
    
    def __str__(self):
        return str(self.components)

# Test the Vector class
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)    # Output: (5, 7, 9)
print(v1 - v2)    # Output: (-3, -3, -3)
print(v1 * 2)     # Output: (2, 4, 6)
