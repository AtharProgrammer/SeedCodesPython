'''
In Python, the find() method is used to find the index of the first occurrence of a substring within a string.
If the substring is found, it returns the index of the first character of the substring; otherwise, it returns -1.

'''
# Example of using find() method
my_string = "Hello, world!"
index = my_string.find("world")
print(index)  # Output: 7

'''
In this example, the find() method searches for the substring "world" within the string my_string.
Since "world" starts at index 7 in my_string, find() returns 7.

If the substring is not found, find() returns -1:
'''
my_string = "Hello, world!"
index = my_string.find("Python")
print(index)  # Output: -1

'''
You can also specify optional arguments to find() to specify the start and end positions for the search:
'''
my_string = "Hello, world!"
index = my_string.find("o", 5)  # Start searching from index 5
print(index)  # Output: 7
