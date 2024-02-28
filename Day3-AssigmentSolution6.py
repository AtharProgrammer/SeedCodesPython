# Input: Number from the user
number = int(input("Enter a number: "))

# Initialize count to 0
count = 0

# Handle the case for 0 explicitly
if number == 0:
    count = 1
else:
    # Loop to count the digits
    while number != 0:
        # Divide the number by 10
        number //= 10
        # Increment the digit count
        count += 1

# Print the number of digits
print(f"The number of digits is: {count}")
