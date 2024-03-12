from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
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
dog = Dog("Buddy")
print(dog.name, "says:", dog.make_sound())

cat = Cat("Whiskers")
print(cat.name, "says:", cat.make_sound())

'''
In this example, Animal is an abstract class with the abstract
method make_sound(). Subclasses Dog and Cat provide concrete
implementations for the make_sound() method.

'''
