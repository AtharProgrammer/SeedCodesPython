'''
Set Operations
Sets support various operations such as union, intersection, difference, and symmetric difference.
'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
