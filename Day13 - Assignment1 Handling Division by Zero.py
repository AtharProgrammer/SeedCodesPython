'''
Assignment 1: Handling Division by Zero
Write a Python program that takes two numbers as input from the user and
calculates their quotient. Handle the ZeroDivisionError exception if the
user enters 0 as the second number.
'''
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Please enter valid numbers")
