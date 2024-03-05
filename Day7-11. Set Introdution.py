'''
What is a Set?
A set is an unordered collection of unique elements. In Python, sets are defined using curly braces {},
and each element is separated by a comma. Sets are mutable, meaning you can add or remove elements from them.

Creating Sets
You can create a set in Python by enclosing comma-separated elements within curly braces {}.
'''

my_set = {1, 2, 3, 4, 5}
print(my_set)

#You can also create an empty set using the set() function:
empty_set = set()
print(empty_set)

#Here's an example demonstrating the unordered nature of sets:
# Define a set with elements in a specific order
my_set = {3, 1, 2}

# Print the set
print(my_set)  # Output: {1, 2, 3}

'''
Adding and Removing Elements
You can add elements to a set using the add() method and remove elements using the remove() or discard() methods.
'''

my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

my_set.discard(4)
print(my_set)  # Output: {1, 2, 5, 6}
