'''
Tuple Operations
While tuples are immutable, you can perform operations like concatenation and repetition.
'''

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

'''
Tuple Methods
Tuples have very few methods because of their immutability.
The primary ones include count() and index().
'''
my_tuple = (1, 2, 2, 3, 4, 2)

# Count occurrences of a value
print(my_tuple.count(2))  # Output: 3

# Get the index of a value
print(my_tuple.index(3))  # Output: 3

#Conversion between data structures
#list(),tuple(),set(),dict()
list1=list(tuple1)
print(list1)
x=input("Enter new element in tuple")
list1.append(x)
print(list1)
print(tuple(list1))
