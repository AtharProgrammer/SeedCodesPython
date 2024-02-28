import math

# Input: Number from the user
number = int(input("Enter a number: "))

# Assume number is prime until proven otherwise
is_prime = True

# Check for edge cases
if number <= 1:
    is_prime = False
else:
    # Only need to check up to the square root of the number
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

# Print the result
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
