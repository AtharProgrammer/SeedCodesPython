'''
In single inheritance, a class inherits from only one parent class.
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass
'''

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog
dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks
