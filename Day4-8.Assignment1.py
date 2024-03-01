# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Using the functions
print(f"The addition of {num1} and {num2} is: {add(num1, num2)}")
print(f"The subtraction of {num1} from {num2} is: {subtract(num1, num2)}")
print(f"The multiplication of {num1} and {num2} is: {multiply(num1, num2)}")
print(f"The division of {num1} by {num2} is: {divide(num1, num2)}")
