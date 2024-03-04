'''
In Python, a list is a versatile and fundamental data structure used to store a collection of items.
Lists are ordered, mutable (changeable), and can contain elements of different data types, such as integers,
strings, or even other lists.
Here's a breakdown of important concepts related to lists:

Creating Lists:
You can create a list by enclosing comma-separated values within square brackets []. For example:
'''
my_list = [1, 2, 3, 4, 5]
print(my_list)
'''
Accessing Elements:
Elements in a list can be accessed using square brackets and indices.
Python uses zero-based indexing, meaning the first element has an index of 0.
Negative indices count from the end of the list. For example:
'''
print(my_list[0])    # Output: 1
print(my_list[-1])   # Output: 5 (last element)

'''
Slicing Lists:
You can extract a subset of elements from a list using slicing. Slicing syntax is list[start:end:step].
Omitting start and end will default to the beginning and end of the list, respectively. For example:
'''

sliced_list = my_list[1:4]  # Returns [2, 3, 4]
print(sliced_list)
