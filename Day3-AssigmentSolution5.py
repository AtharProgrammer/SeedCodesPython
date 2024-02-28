import math

# Input: Two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD
gcd = math.gcd(num1, num2)

# Print the GCD
print(f"The Greatest Common Divisor (GCD) of {num1} and {num2} is: {gcd}")
