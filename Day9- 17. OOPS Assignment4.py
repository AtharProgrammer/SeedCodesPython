'''
Assignment:
Create a class called Car with attributes make, model, and year.
Implement methods to get and set each attribute. Also,
implement a method to display the car's information.
'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Test the Car class
car1 = Car("Toyota", "Camry", 2020)
car1.display_info()

car2 = Car("Honda", "Accord", 2018)
car2.set_year(2019)
print("Updated year:", car2.get_year())
