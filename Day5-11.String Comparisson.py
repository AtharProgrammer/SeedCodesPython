'''
In Python, you can compare strings using comparison operators such as ==, !=, <, >, <=, and >=.
These operators compare strings lexicographically based on their Unicode code points.

In this example, strings are compared based on their lexicographic order, where 'a' comes before 'b'.
Therefore, "apple" is less than "banana", and the comparison results reflect that.
When comparing strings, Python compares the Unicode code points of the characters in the strings one by one until
it finds a difference or reaches the end of one of the strings.
'''

# Example of string comparison
str1 = "apple"
str2 = "banana"

# Equal to
print(str1 == str2)  # Output: False

# Not equal to
print(str1 != str2)  # Output: True

# Less than
print(str1 < str2)   # Output: True

# Greater than
print(str1 > str2)   # Output: False

# Less than or equal to
print(str1 <= str2)  # Output: True

# Greater than or equal to
print(str1 >= str2)  # Output: False
