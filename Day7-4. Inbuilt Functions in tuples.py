#len(): Returns the number of elements in the tuple.
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # Output: 5

#sorted(): Returns a new sorted list from the elements of the tuple.
my_tuple = (3, 2, 1, 4, 5)
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)  # Output: [1, 2, 3, 4, 5]

#max(): Returns the maximum value from the tuple.
my_tuple = (10, 30, 20, 50, 40)
print(max(my_tuple))  # Output: 50

#min(): Returns the minimum value from the tuple.
my_tuple = (10, 30, 20, 50, 40)
print(min(my_tuple))  # Output: 10


#sum(): Returns the sum of all elements in the tuple.
my_tuple = (1, 2, 3, 4, 5)
print(sum(my_tuple))  # Output: 15

'''
enumerate(): Returns an enumerate object containing tuples of the
index and corresponding elements of the original tuple.
'''
my_tuple = ('a', 'b', 'c')
for index, value in enumerate(my_tuple):
    print(index, value)
# Output:
# 0 a
# 1 b
# 2 c

#reversed(): Returns an iterator that iterates over the elements of the tuple in reverse order.
my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple)  # Output: (5, 4, 3, 2, 1)

#zip(): Combines elements from multiple tuples into tuples of corresponding elements.
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped_tuple = tuple(zip(tuple1, tuple2))
print(zipped_tuple)  # Output: ((1, 'a'), (2, 'b'), (3, 'c'))




