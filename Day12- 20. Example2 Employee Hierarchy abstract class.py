'''
In this example, Employee is an abstract class with the abstract method
calculate_salary(). Subclasses FullTimeEmployee and PartTimeEmployee
provide concrete implementations
for calculating salary.
'''

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, name, salary, hours_worked):
        super().__init__(name, salary)
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.salary * self.hours_worked

# Usage
full_time_emp = FullTimeEmployee("Alice", 50000)
print(full_time_emp.name, "earns:", full_time_emp.calculate_salary())

part_time_emp = PartTimeEmployee("Bob", 20, 25)
print(part_time_emp.name, "earns:", part_time_emp.calculate_salary())
