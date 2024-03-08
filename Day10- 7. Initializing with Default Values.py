class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# Creating an instance of Point with default values
point1 = Point()
print(point1.x, point1.y)  # Output: 0 0

# Creating an instance of Point with custom values
point2 = Point(3, 4)
print(point2.x, point2.y)  # Output: 3 4
