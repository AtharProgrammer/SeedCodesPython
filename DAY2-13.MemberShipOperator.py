'''

in operator: Returns True if the specified value is found in the sequence.
not in operator: Returns True if the specified value is not found in the sequence.

'''

# For a string
print('a' in 'apple')  # Output: True

# For a list
print(1 in [1, 2, 3])  # Output: True

# For a tuple
print(4 in (1, 2, 3))  # Output: False

# For a dictionary (checks among keys)
print('key' in {'key': 'value'})  # Output: True

# For a set
print(3 in {1, 2, 3})  # Output: True

# For a string
print('b' not in 'apple')  # Output: True

# For a list
print(4 not in [1, 2, 3])  # Output: True

# For a tuple
print(1 not in (2, 3, 4))  # Output: True

# For a dictionary (checks among keys)
print('value' not in {'key': 'value'})  # Output: True

# For a set
print(5 not in {1, 2, 3})  # Output: True
