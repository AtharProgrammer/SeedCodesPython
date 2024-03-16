'''
File handling in Python allows you to work with files on your filesystem, including reading from and writing to them.
Python provides built-in functions and methods to perform various operations on files. Here's an overview of file handling in Python:
'''

### Opening a File
'''
You can open a file using the `open()` function. It takes two arguments: the path to the file and the mode
in which you want to open the file (e.g., read, write, append).
'''
# Open a file in read mode
file = open('example.txt', 'r')

### Reading from a File
'''
Once a file is opened, you can read its contents using various methods such as `read()`, `readline()`, or `readlines()`.
'''
# Read the entire contents of the file
content = file.read()

# Read a single line from the file
line = file.readline()



### Writing to a File
#To write to a file, open it in write or append mode and use the `write()` method.

# Open a file in write mode
file = open('example.txt', 'w')

# Write content to the file
file.write('Hello, world!\n')
file.write('This is a new line.\n')

### Closing a File

#After performing file operations, it's essential to close the file using the `close()` method to free up system resources.

file.close()


### Using `with` Statement
#A better practice is to use the `with` statement, which ensures that the file is properly closed after its suite finishes, even if an exception is raised.

with open('example.txt', 'r') as file:
    content = file.read()
    # File automatically closed after this block


### File Modes
'''
Here are some common file modes:

- `'r'`: Read mode (default). Opens a file for reading.
- `'w'`: Write mode. Opens a file for writing. Creates a new file or truncates an existing file.
- `'a'`: Append mode. Opens a file for writing. Creates a new file if it does not exist.
- `'b'`: Binary mode. Opens a file in binary mode.
- `'+'`: Update mode. Opens a file for both reading and writing.
'''
### Error Handling

#You should handle file-related errors, such as FileNotFoundError or PermissionError, using try-except blocks.


try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()


### Using `os` Module
#The `os` module provides functions for file-related operations like renaming and deleting files, checking if a file exists, and more.


import os

# Check if the file exists before renaming
if os.path.exists('old_file.txt'):
    os.rename('old_file.txt', 'new_file.txt')
    print("File renamed successfully.")
else:
    print("The file 'old_file.txt' does not exist.")


# Delete a file
os.remove('file_to_delete.txt')

# Check if a file exists
if os.path.exists('example.txt'):
    print("File exists")
'''
Remember to handle file paths properly, especially when working with directories or when your script
is expected to run on different operating systems. Python's `os.path` module can be helpful for this purpose.
'''
