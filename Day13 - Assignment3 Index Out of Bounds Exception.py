'''
Assignment 3: Index Out of Bounds Exception
Write a Python program that prompts the user to enter a list of numbers
and then prints the element at a specified index. Handle the IndexError
exception if the user enters an invalid index.
'''
try:
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    index = int(input("Enter the index to retrieve: "))
    
    value = numbers[index]
    print("Value at index", index, ":", value)
except IndexError:
    print("Error: Index out of bounds")
except ValueError:
    print("Error: Please enter a valid index")
