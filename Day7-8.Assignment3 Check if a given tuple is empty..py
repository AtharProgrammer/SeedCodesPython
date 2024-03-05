'''
Assignment 3: Check if a given tuple is empty.
Problem:
Write a Python function to check if a given tuple is empty.

Solution:

'''
def is_empty_tuple(input_tuple):
    return len(input_tuple) == 0

empty_tuple = ()
non_empty_tuple = (1, 2, 3)

print(is_empty_tuple(empty_tuple))  # Output: True
print(is_empty_tuple(non_empty_tuple))  # Output: False
