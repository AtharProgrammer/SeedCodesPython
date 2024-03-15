'''
Abstract classes in Python are classes that cannot be instantiated on their own.
They serve as blueprints for other classes and typically define methods that must be implemented by their subclasses.
Abstract classes are created using the abc module in Python, which stands for Abstract Base Classes.

Here's a brief tutorial on how to create and use abstract classes in Python:

Step 1: Import the abc Module
'''

from abc import ABC, abstractmethod

# Step 2: Define an Abstract Class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Step 3: Create Subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Step 4: Use the Subclasses

circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

'''
In this example, Shape is an abstract class with two abstract methods area() and perimeter().
These methods must be implemented by any subclass of Shape. The Circle and Rectangle classes are subclasses of Shape,
and they provide concrete implementations for the abstract methods.

Attempting to instantiate an abstract class directly will result in an error:
'''
# This will raise an error because Shape is an abstract class
#shape = Shape()

'''
Abstract classes are useful when you want to enforce certain methods to be implemented by subclasses,
ensuring a consistent interface across different classes. They are commonly used in design patterns and
frameworks where you want to define a common interface that multiple classes must adhere to.
'''
