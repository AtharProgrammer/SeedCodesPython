'''
You can perform various operations on lists, including concatenation (+),
repetition (*), membership testing (in), and iteration using loops.
'''
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = [0] * 3
print(repeated_list)  # Output: [0, 0, 0]

# Membership testing
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)   # Output: True
print(6 in my_list)   # Output: False

# Iteration using loops
for item in my_list:
    print(item)
