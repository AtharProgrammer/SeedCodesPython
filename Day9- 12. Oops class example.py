'''
Classes:
A class is a blueprint for creating objects (instances).
It defines the properties (attributes) and behaviors (methods) that objects of the class will have.
Classes are created using the class keyword followed by the class name.
Example:
'''
class Person:
    # here self is zero positional argument
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

'''
Objects (Instances):
An object is an instance of a class.
It represents a specific entity with its own set of data and behavior, based on the class blueprint.
Objects are created by calling the class as if it were a function.
Example:
'''
person1 = Person("Alice", 30)
print(person1.greet())
person2 = Person("Bob", 25)
print(person2.greet())
