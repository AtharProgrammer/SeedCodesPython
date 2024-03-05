'''
Assignment 5: Intersection of Multiple Sets
Problem:
Write a Python function to find the intersection of multiple sets.

Solution:
'''

def intersection_of_sets(sets):
    if not sets:
        return set()
    result = sets[0]
    for s in sets[1:]:
        result = result.intersection(s)
    return result

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

print(intersection_of_sets([set1, set2, set3]))  # Output: {3}
