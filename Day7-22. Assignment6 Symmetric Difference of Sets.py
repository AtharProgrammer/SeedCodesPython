'''
Assignment 6: Symmetric Difference of Sets
Problem:
Write a Python function to find the symmetric difference of two sets.

Solution:
'''
def symmetric_difference(set1, set2):
    return (set1 - set2).union(set2 - set1)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(symmetric_difference(set1, set2))  # Output: {1, 4}
