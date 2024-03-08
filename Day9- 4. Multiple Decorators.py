'''

Multiple Decorators:
You can apply multiple decorators to a single function or method by
stacking them on top of each other:

'''

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2

def my_function():
    print("Original Function")

my_function()
