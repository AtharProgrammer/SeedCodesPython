'''
4. Handling Exceptions with Else Clause
You can use the else clause to run code that should only execute if no exceptions were raised.

'''

try:
    pass
    # Some code
except Exception:
    # Exception handling
    print("An error occurred")
else:
    # Code to execute if no exceptions occurred
    print("No errors occurred")
