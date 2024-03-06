#Sorting a List of Tuples by Second Element

pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
