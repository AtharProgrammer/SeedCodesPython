'''
To determine if a given year is a leap year or not in Python,
you can follow these rules:

A year that is divisible by 4 is a leap year.
However, if the year is also divisible by 100, it is not a leap year.
Yet, if the year is divisible by 400, it is a leap year.
'''
# Input: Year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
