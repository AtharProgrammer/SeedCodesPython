# Creating an empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Creating a dictionary with initial key-value pairs
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Using the dict() constructor
another_dict = dict(name='Alice', age=25, city='Los Angeles')
print(another_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}

# Accessing an element
print(my_dict['name'])  # Output: John

# Using get() returns None instead of KeyError if the key is not found
print(my_dict.get('profession'))  # Output: None
