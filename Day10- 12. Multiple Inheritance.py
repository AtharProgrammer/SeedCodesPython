'''
Multiple Inheritance:
Multiple inheritance allows a class to inherit from multiple parent classes.

class ParentClass1:
    pass

class ParentClass2:
    pass

class ChildClass(ParentClass1, ParentClass2):
    pass
'''

class Swim:
    def swim(self):
        print("Swimming")

class Fly:
    def fly(self):
        print("Flying")

class Duck(Swim, Fly):
    pass

# Creating an instance of Duck
duck = Duck()
duck.swim()  # Output: Swimming
duck.fly()   # Output: Flying
