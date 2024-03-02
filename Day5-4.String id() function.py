'''
The id() function in Python returns the identity (unique integer) of an object.
This identity is unique and constant for the lifetime of the object.
'''

# Example of using id() with different types of objects

# Integer objects
x = 42
print(id(x))  # Output: A unique integer representing the identity of the integer object

# String objects
s = "Hello"
print(id(s))  # Output: A unique integer representing the identity of the string object

# List objects
lst = [1, 2, 3]
print(id(lst))  # Output: A unique integer representing the identity of the list object

'''
The id() function is particularly useful when you want to check if two
variables reference the same object.
If two variables have the same id(), they refer to the same object in memory:
'''
a = [1, 2, 3]
b = a  # b now references the same object as a
print(id(a) == id(b))  # Output: True
