# Input: Number from the user
number = int(input("Enter a number: "))

# Initialize the factorial value
factorial = 1

# Check if the number is negative, zero or positive
if number < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate factorial using a while loop
    temp = number  # Temporary variable to decrement in the loop
    while temp > 0:
        factorial *= temp
        temp -= 1

    # Print the factorial
    print(f"The factorial of {number} is {factorial}.")
