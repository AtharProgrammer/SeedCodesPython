# Creating a dictionary
my_dict = {"apple": 5, "banana": 10, "orange": 7}

# Using the get() method to access values safely
print(my_dict.get("apple", "Not found"))  # Output: 5
print(my_dict.get("grape", "Not found"))  # Output: Not found


# Using the pop() method to remove and return a value
value = my_dict.pop("banana")
print("Popped value:", value)  # Output: Popped value: 10
print("Dictionary after pop:", my_dict)  # Output: {'apple': 5, 'orange': 7}

# Using the update() method to merge dictionaries
other_dict = {"grape": 3, "peach": 6}
my_dict.update(other_dict)
print("Merged dictionary:", my_dict)  # Output: {'apple': 5, 'orange': 7, 'grape': 3, 'peach': 6}
