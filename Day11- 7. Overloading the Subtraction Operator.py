class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the subtraction operator
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

# Creating two instances of the Vector class
v1 = Vector(5, 3)
v2 = Vector(2, 4)

# Using the overloaded - operator
result = v1 - v2

print(result.x, result.y)  # Output: 3 -1
