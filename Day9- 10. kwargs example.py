'''
In Python, *args and **kwargs allow you to pass a variable number
of arguments to a function.
'''

'''
*args:

It is used to pass a variable number of non-keyword arguments to a function.
The *args parameter collects all the positional arguments passed to the function into a tuple.
You can use any name instead of args, but args is a convention.
Example:
'''

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)  # Output: 1 2 3

'''
**kwargs:

It is used to pass a variable number of keyword arguments (or named arguments)
to a function.The **kwargs parameter collects all the keyword arguments
passed to the function into a dictionary where the keys are the argument names.
You can use any name instead of kwargs, but kwargs is a convention.
Example:
'''
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name="Alice", age=30)  # Output: name Alice, age 30


'''
Combining them, you can create functions that accept any number of both positional and keyword arguments:
'''
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

my_function(1, 2, 3, name="Alice", age=30)  # Output: 1 2 3, name Alice, age 30
