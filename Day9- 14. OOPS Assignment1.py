'''
Assignment:
Create a class called Rectangle with attributes length and width.
Implement methods to calculate the area and perimeter of the rectangle.
Also, create a method to check if the rectangle is a square.

'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

# Test the Rectangle class
rectangle1 = Rectangle(5, 5)
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())
print("Is square?", rectangle1.is_square())  # True

rectangle2 = Rectangle(4, 6)
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())
print("Is square?", rectangle2.is_square())  # False
