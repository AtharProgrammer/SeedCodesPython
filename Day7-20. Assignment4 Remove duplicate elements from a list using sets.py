'''
Assignment 4: Remove duplicate elements from a list using sets.
Problem:
Write a Python function to remove duplicate elements from a list using sets.

Solution:
'''

def remove_duplicates(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = remove_duplicates(my_list)
print(unique_elements)  # Output: [1, 2, 3, 4, 5]
