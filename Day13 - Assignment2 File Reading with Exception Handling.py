'''
Assignment 2: File Reading with Exception Handling
Write a Python program that reads the contents of a file named data.txt
and prints them. Handle the FileNotFoundError exception if the file does
not exist.
'''

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print("Error:", e)


