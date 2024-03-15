'''
In Python, abstract methods are methods defined in a base class,
but they lack implementation details. Instead, they're meant to be
overridden by subclasses. Abstract methods serve as a blueprint for subclasses,
ensuring that they implement certain functionality.

To create an abstract method in Python, you need to use the abstractmethod decorator
from the abc module. Here's a simple example:

'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog()
print(dog.make_sound())  # Output: Woof!

cat = Cat()
print(cat.make_sound())  # Output: Meow!

'''
In this example, Animal is an abstract base class with the abstract method make_sound().
Subclasses Dog and Cat provide concrete implementations for the make_sound() method.

Attempting to instantiate Animal directly will result in an error:
'''

#animal = Animal()  # This will raise an error

'''
Abstract methods are useful when you want to define a common interface for a group of related classes, ensuring that all subclasses
implement certain functionality. They promote code reusability and maintainability by enforcing a
consistent interface across different implementations.
'''

