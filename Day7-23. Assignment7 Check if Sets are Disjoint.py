'''
Assignment 7: Check if Sets are Disjoint
Problem:
Write a Python function to check if two sets are disjoint (i.e., they have no common elements).

Solution:
'''
def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

print(are_disjoint(set1, set2))  # Output: True
print(are_disjoint(set1, set3))  # Output: False
