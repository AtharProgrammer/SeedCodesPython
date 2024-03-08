class Person:
# constructor of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of Person
person = Person("Alice", 30)

# Accessing instance variables
print(person.name)  # Output: Alice
print(person.age)   # Output: 30
