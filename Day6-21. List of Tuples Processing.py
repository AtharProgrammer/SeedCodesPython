'''
List of Tuples Processing: Manipulate lists of tuples by sorting, filtering, or transforming elements.
'''

# Sorting a list of tuples by the second element
list_of_tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
print(sorted_list)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]

# Filtering a list of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
filtered_list = [tup for tup in list_of_tuples if tup[0] % 2 == 0]
print(filtered_list)  # Output: [(2, 'b')]

# Transforming a list of tuples to a list of strings
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
list_of_strings = [str(num) + char for num, char in list_of_tuples]
print(list_of_strings)  # Output: ['1a', '2b', '3c']
