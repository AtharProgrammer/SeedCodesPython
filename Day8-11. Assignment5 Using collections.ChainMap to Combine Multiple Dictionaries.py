from collections import ChainMap

# Combining multiple dictionaries using ChainMap
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined_dict = ChainMap(dict1, dict2)
print("Combined dictionary:", dict(combined_dict))  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
