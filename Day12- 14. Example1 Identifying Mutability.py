# Lists are mutable objects
list1 = [1, 2, 3]
list2 = list1
print(id(list1))  # Output: A unique identifier for list1
print(id(list2))  # Output: The same unique identifier for list2 as list1

list1.append(4)
print(id(list1))  # Output: The identifier remains the same after modification
print(id(list2))  # Output: The identifier remains the same for list2 as well


