'''
Assignment:
Create a class called Employee with attributes name, position, and salary.
Implement methods to give a salary raise to the employee and display the
employee's information.

'''
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, raise_amount):
        self.salary += raise_amount
        print(f"Salary of {self.name} has been raised by {raise_amount}. New salary: {self.salary}")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")

# Test the Employee class
employee1 = Employee("John Doe", "Manager", 50000)
employee1.display_info()
employee1.give_raise(2000)

employee2 = Employee("Alice Smith", "Developer", 60000)
employee2.display_info()
employee2.give_raise(3000)
