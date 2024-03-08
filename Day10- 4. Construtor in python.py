'''
In Python, constructors are special methods used for initializing objects
when they are created. Constructors in Python are defined
using the __init__ method within a class. When you create a
new instance of a class, Python automatically calls the __init__ method
for that class if it's defined.
'''
class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
    def printdata(self):
        print(self.param1)

# Creating an instance of MyClass
obj = MyClass(10, "hello")
obj.printdata()
# Accessing instance variables
print(obj.param1)  # Output: 10
print(obj.param2)  # Output: hello

'''
In this example, the __init__ method takes three parameters:
self (which refers to the instance being created) and two additional
parameters param1 and param2. Inside the constructor, we initialize
instance variables param1 and param2
with the values passed during object creation.

Constructors can perform any necessary initialization for the object.
This can include initializing instance variables, setting up resources,
or performing any other setup required for the object to be in a valid state.
'''
