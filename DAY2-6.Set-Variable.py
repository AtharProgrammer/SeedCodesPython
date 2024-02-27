# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

# Creating a set with elements
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Using the set() constructor
another_set = set([1, 2, 2, 3, 4])  # Duplicates are removed
print(another_set)  # Output: {1, 2, 3, 4}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (elements in either a or b)
print(a | b)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (elements in both a and b)
print(a & b)  # Output: {3, 4}

# Difference (elements in a but not in b)
print(a - b)  # Output: {1, 2}

# Symmetric Difference (elements in a or b but not both)
print(a ^ b)  # Output: {1, 2, 5, 6}
