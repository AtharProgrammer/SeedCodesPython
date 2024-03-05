'''
Assignment 3: Check if one set is a subset of another set.
Problem:
Write a Python function to check if one set is a subset of another set.

Solution:

'''
def is_subset(set1, set2):
    return set1.issubset(set2)

set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}

print(is_subset(set1, set2))  # Output: True
