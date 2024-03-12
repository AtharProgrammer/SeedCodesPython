'''
Assignment 1: Complex Number Class
Description: Create a class representing complex numbers.
Implement methods to overload the basic arithmetic operators (+, -, *)
for complex number arithmetic.

Solution:
'''
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Test the ComplexNumber class
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)

print(c1 + c2)  # Output: 6 + 8i
print(c1 - c2)  # Output: -2 - 2i
print(c1 * c2)  # Output: -7 + 22i
