#zip(): Combines elements from multiple tuples into tuples of corresponding elements.
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped_tuple = tuple(zip(tuple1, tuple2))
print(zipped_tuple)  # Output: ((1, 'a'), (2, 'b'), (3, 'c'))


# To unzip-

'''
In the code above, *zipped_tuple passes each tuple from zipped_tuple as separate arguments to zip(),
effectively "unzipping" it. Then zip() pairs up corresponding elements from each argument,
effectively undoing the zipping operation.
'''

# Unzip the zipped tuple
unzipped_tuple = tuple(zip(*zipped_tuple))

#Now unzipped_tuple will contain the original tuples before they were zipped:
print(unzipped_tuple)

