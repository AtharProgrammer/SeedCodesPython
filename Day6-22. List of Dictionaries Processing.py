'''
List of Dictionaries Processing: Perform operations like filtering and sorting on lists of dictionaries.
'''

# Filtering a list of dictionaries based on a condition
list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
filtered_list = [d for d in list_of_dicts if d['age'] > 28]
print(filtered_list)  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Sorting a list of dictionaries by a specific key
list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_list = sorted(list_of_dicts, key=lambda x: x['age'])
print(sorted_list)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
