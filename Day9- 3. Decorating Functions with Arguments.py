'''
Decorating Functions with Arguments:
If the function you're decorating takes arguments,
you can use *args and **kwargs to capture any number of positional
and keyword arguments:
'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator


def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
