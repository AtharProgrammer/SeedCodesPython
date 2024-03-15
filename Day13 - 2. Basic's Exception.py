'''
Exception handling in Python allows you to gracefully manage errors
that may occur during the execution of your code. Here's a tutorial
on exception handling in Python:

1. Basic Syntax
Python provides a try, except block for handling exceptions.
Code that might raise an exception is placed inside the try block,
and the handling of the exception is done in the except block.
'''
try:
    # Code that might raise an exception
    result = 10 / 0
except:
    # Handling the exception
    print("An error occurred")
