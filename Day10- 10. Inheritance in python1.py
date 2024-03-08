'''
Inheritance is a fundamental concept in object-oriented programming (OOP)
that allows a class (subclass or child class) to inherit attributes
and methods from another class (superclass or parent class).
In Python, inheritance is implemented using the following syntax:


class ParentClass:
    # Attributes and methods of the parent class

class ChildClass(ParentClass):
    # Additional attributes and methods of the child class

'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

# Dog class inherits from Animal class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Cat class inherits from Animal class
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Accessing methods from parent class
dog.speak()  # Output: Animal speaks
cat.speak()  # Output: Animal speaks

# Accessing methods specific to child classes
dog.bark()  # Output: Dog barks
cat.meow()  # Output: Cat meows

'''
In this example, Dog and Cat are subclasses of Animal. They inherit the speak() method from the Animal class and
also have their own specific methods bark() and meow().
Instances of Dog and Cat can access methods defined in both the parent and child classes.
'''
