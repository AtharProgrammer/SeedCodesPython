'''
Assignment 2: Find the maximum and minimum elements in a tuple.
Problem:
Write a Python function to find the maximum and minimum elements in a tuple.

Solution:

'''

def max_min_tuple(input_tuple):
    return max(input_tuple), min(input_tuple)

my_tuple = (10, 30, 20, 50, 40)
max_element, min_element = max_min_tuple(my_tuple)
print("Maximum element:", max_element)  # Output: Maximum element: 50
print("Minimum element:", min_element)  # Output: Minimum element: 10
