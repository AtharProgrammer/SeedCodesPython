'''
Assignment 1: Find the union of two sets.
Problem:
Write a Python function to find the union of two sets.

Solution:
'''

def union_of_sets(set1, set2):
    return set1.union(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_result = union_of_sets(set1, set2)
print(union_result)  # Output: {1, 2, 3, 4, 5}
