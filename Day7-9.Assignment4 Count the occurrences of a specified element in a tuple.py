'''
Assignment 4: Count the occurrences of a specified element in a tuple.
Problem:
Write a Python function to count the occurrences of a specified element in a tuple.

Solution:
'''

def count_occurrences(input_tuple, element):
    return input_tuple.count(element)

my_tuple = (1, 2, 2, 3, 4, 2)
element_to_count = 2

print("Occurrences of", element_to_count, ":", count_occurrences(my_tuple, element_to_count))  # Output: Occurrences of 2: 3
