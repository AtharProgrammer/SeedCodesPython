'''
Problem 1: Vehicle Inheritance Hierarchy
Define a class Vehicle with attributes make and model, and a method
display_info() to print the make and model of the vehicle.
Then, define two subclasses Car and Motorcycle.
Implement the display_info() method in both subclasses to
include additional
information specific to each vehicle type.
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, num_wheels):
        super().__init__(make, model)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.num_wheels}")

# Test
car = Car("Toyota", "Camry", 4)
car.display_info()

motorcycle = Motorcycle("Honda", "CBR500R", 2)
motorcycle.display_info()
