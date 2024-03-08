'''
Assignment:
Create a class called Triangle with attributes side1, side2, and side3.
Implement methods to calculate the perimeter and area of the triangle.
Also, create a method to check if the triangle is equilateral (all sides are equal).
'''
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        # Using Heron's formula to calculate the area of the triangle
        s = self.perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def is_equilateral(self):
        return self.side1 == self.side2 == self.side3

# Test the Triangle class
triangle1 = Triangle(3, 4, 5)
print("Perimeter:", triangle1.perimeter())
print("Area:", triangle1.area())
print("Is equilateral?", triangle1.is_equilateral())  # False

triangle2 = Triangle(5, 5, 5)
print("Perimeter:", triangle2.perimeter())
print("Area:", triangle2.area())
print("Is equilateral?", triangle2.is_equilateral())  # True
