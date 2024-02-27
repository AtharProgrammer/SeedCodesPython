# An empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# A tuple with one element (note the trailing comma)
singleton_tuple = (1,)
print(singleton_tuple)  # Output: (1,)

# A tuple with multiple elements
my_tuple = (1, "Hello", 3.14)
print(my_tuple)  # Output: (1, 'Hello', 3.14)

# Parentheses are optional for tuples, but recommended for clarity
another_tuple = 1, "Hello", 3.14
print(another_tuple)  # Output: (1, 'Hello', 3.14)

# Accessing the first element
print(my_tuple[0])  # Output: 1

# Accessing a slice of the tuple
print(my_tuple[1:3])  # Output: ('Hello', 3.14)

# Negative indexing
print(my_tuple[-1])  # Output: 3.14
