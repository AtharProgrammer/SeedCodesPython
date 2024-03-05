'''
Assignment 1: Merge two tuples into a single tuple.

Problem:
Write a Python function to merge two tuples.

'''

#Solution

def merge_tuples(tuple1, tuple2):
    return tuple1 + tuple2

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

merged_tuple = merge_tuples(tuple1, tuple2)
print(merged_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')
