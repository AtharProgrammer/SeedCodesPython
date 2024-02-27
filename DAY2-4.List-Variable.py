#Creating Lists
#Lists are defined by enclosing elements in square brackets [], with items separated by commas.

# An empty list
my_list = []
print(my_list)  # Output: []

# A list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]

# A list with mixed data types
mixed_list = [1, "Hello", 3.14, [1, 2, 3]]
print(mixed_list)  # Output: [1, 'Hello', 3.14, [1, 2, 3]]

#Accessing List Elements
#You can access individual elements of a list using indexing and slicing, similar to strings. Python lists are zero-indexed.

# Accessing the first element
print(numbers[0])  # Output: 1

# Accessing a slice of the list
print(numbers[1:3])  # Output: [2, 3]

# Negative indexing (accessing from the end)
print(numbers[-1])  # Output: 5
