class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True  # Additional initialization

    def feed(self):
        self.is_hungry = False

# Creating an instance of Dog
dog = Dog("Buddy", 3)

# Accessing instance variables
print(dog.name)        # Output: Buddy
print(dog.age)         # Output: 3
print(dog.is_hungry)   # Output: True

# Feeding the dog
dog.feed()
print(dog.is_hungry)   # Output: False
