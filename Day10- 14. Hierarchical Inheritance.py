'''
Hierarchical Inheritance:
Hierarchical inheritance involves
multiple subclasses inheriting from a single superclass.

class ParentClass:
    pass

class ChildClass1(ParentClass):
    pass

class ChildClass2(ParentClass):
    pass

'''

class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating instances of Cat and Dog
cat = Cat()
dog = Dog()

cat.speak()  # Output: Animal speaks
cat.meow()   # Output: Cat meows

dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks
