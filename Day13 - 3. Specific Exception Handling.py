'''
2. Specific Exception Handling
You can catch specific exceptions and handle them differently.

'''

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("An error occurred:", e)
