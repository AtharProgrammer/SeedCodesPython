# Creating a dictionary
my_dict = {"apple": 5, "banana": 10, "orange": 7}

# Accessing values using keys
print(my_dict["apple"])  # Output: 5
print(my_dict["banana"])  # Output: 10

# Adding a new key-value pair
my_dict["grape"] = 3

# Updating an existing value
my_dict["banana"] = 15

# Removing a key-value pair
del my_dict["orange"]

# Iterating over keys
for key in my_dict:
    print(key, "->", my_dict[key])

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, "->", value)

# Checking if a key exists
if "apple" in my_dict:
    print("Yes, 'apple' is present in the dictionary")

# Getting the number of key-value pairs
print("Number of items in the dictionary:", len(my_dict))

# Clearing the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)
