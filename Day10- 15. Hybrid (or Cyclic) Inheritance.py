'''

Hybrid (or Cyclic) Inheritance:
Hybrid inheritance is a combination of multiple types of inheritance,
including single, multiple, multilevel, or hierarchical inheritance.
It's generally
recommended to avoid hybrid inheritance due to potential complexities.

class ParentClass1:
    pass

class ParentClass2:
    pass

class ChildClass1(ParentClass1):
    pass

class ChildClass2(ParentClass1, ParentClass2):
    pass

'''

class Animal:
    def speak(self):
        print("Animal speaks")

class Fly:
    def fly(self):
        print("Flying")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Bat(Animal, Fly):
    pass

# Creating instances of Dog and Bat
dog = Dog()
bat = Bat()

dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks

bat.speak()  # Output: Animal speaks
bat.fly()    # Output: Flying
