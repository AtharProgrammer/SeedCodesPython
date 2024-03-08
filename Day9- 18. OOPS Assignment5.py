'''
Create a class called Circle with attributes radius and color.
Implement methods to calculate the area and circumference of the circle.
Also, create a method to change the color of the circle.
'''
import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def change_color(self, new_color):
        self.color = new_color
        print(f"The color of the circle has been changed to {self.color}")

# Test the Circle class
circle1 = Circle(5, "red")
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())
circle1.change_color("blue")

circle2 = Circle(3, "green")
print("Area:", circle2.area())
print("Circumference:", circle2.circumference())
