class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overloading the equality operator
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

# Creating two instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Alice", 20)
student3 = Student("Bob", 22)

# Using the overloaded == operator
print(student1 == student2)  # Output: True
print(student1 == student3)  # Output: False
