'''
Python provides a variety of built-in string functions/methods that allow you to manipulate strings efficiently.
Here are some commonly used ones:
'''
#len(): Returns the length of the string.
my_string = "Hello, world!"
print(len(my_string))  # Output: 13

#capitalize(): Returns a copy of the string with the first character capitalized.
my_string = "Hello, World!"
print(my_string.capitalize())  # Output: "Hello, world!"

#upper() and lower(): Returns a copy of the string converted to uppercase or lowercase, respectively.
my_string = "Hello, World!"
print(my_string.upper())  # Output: "HELLO, WORLD!"
print(my_string.lower())  # Output: "hello, world!"

#strip(): Returns a copy of the string with leading and trailing whitespace removed.
my_string = "   Hello, world!   "
print(my_string.strip())  # Output: "Hello, world!"

#replace(): Returns a copy of the string with all occurrences of a substring replaced with another substring.
my_string = "Hello, world!"
new_string = my_string.replace("world", "Python")
print(new_string)  # Output: "Hello, Python!"

#split(): Splits the string into a list of substrings based on a delimiter.
my_string = "Hello, world!"
words = my_string.split(", ")
print(words)  # Output: ['Hello', 'world!']

#join(): Joins elements of a list into a single string using a specified delimiter.
words = ['Hello', 'world!']
my_string = ", ".join(words)
print(my_string)  # Output: "Hello, world!"
