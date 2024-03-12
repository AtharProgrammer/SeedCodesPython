'''
Operator overloading in Python allows you to define custom behavior
for built-in operators like +, -, *, /, etc., when used with instances of
your classes. This feature enables objects to behave like native types,
providing intuitive and concise syntax for operations.

Here's an example demonstrating how to overload the + operator for a
custom class:
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Creating two instances of the Point class
point1 = Point(1, 2)
point2 = Point(3, 4)

# Using the overloaded + operator
result = point1 + point2

print(result.x, result.y)  # Output: 4 6

'''
In this example, __add__ is the special method for overloading the + operator. When point1 + point2 is executed,
Python internally calls point1.__add__(point2).

Similarly, you can overload other operators like -
(__sub__), * (__mul__), / (__truediv__), == (__eq__), != (__ne__), < (__lt__), > (__gt__), etc., by
defining the corresponding special methods in your class.

Here are some common special methods for operator overloading:

__add__(self, other): Implement addition.
__sub__(self, other): Implement subtraction.
__mul__(self, other): Implement multiplication.
__truediv__(self, other): Implement division.
__eq__(self, other): Implement equality.
__lt__(self, other): Implement less than.
__gt__(self, other): Implement greater than.
__str__(self): Implement string representation.
By defining these special methods in your classes, you can customize how instances of your classes behave when used with built-in
operators, providing
flexibility and allowing for more natural and expressive code.
'''
