'''
7. Custom Exceptions
You can create custom exception classes by subclassing built-in exceptions.
'''
class CustomError(Exception):
    pass

# Raise custom exception
raise CustomError("This is a custom error message")
