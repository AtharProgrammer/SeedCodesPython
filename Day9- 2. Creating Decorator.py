'''
Creating a Decorator:
A decorator is a function that takes another function as an argument
and returns a new function. Here's a basic example
'''


def my_decorator(func):
    def function1():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return function1

# Annotation
@my_decorator
def say_hello():
    print("Hello!")
    
print("Execution start from here")
say_hello()

