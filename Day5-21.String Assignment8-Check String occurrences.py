# Example of counting occurrences of a character
my_string = "hello, world!"
count_e = my_string.count('e')
print(count_e)  # Output: 1

# Example of counting occurrences of a substring
count_llo = my_string.count('llo')
print(count_llo)  # Output: 1

# Count occurrences with optional arguments
count_l = my_string.count('l', 3)  # Start counting from index 3
print(count_l)  # Output: 2
