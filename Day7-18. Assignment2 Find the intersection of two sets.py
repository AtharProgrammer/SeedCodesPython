'''
Assignment 2: Find the intersection of two sets.
Problem:
Write a Python function to find the intersection of two sets.

Solution:
'''
def intersection_of_sets(set1, set2):
    return set1.intersection(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_result = intersection_of_sets(set1, set2)
print(intersection_result)  # Output: {3}
