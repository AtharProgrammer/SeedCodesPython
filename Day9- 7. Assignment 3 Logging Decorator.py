'''
Assignment 3: Logging Decorator
Write a Python decorator that logs the function call and its arguments.
'''

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def example_function(x, y):
    return x + y

# Test the function
print(example_function(3, 5))
