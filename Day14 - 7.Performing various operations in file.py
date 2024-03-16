
def create_file():
    file_name = input("Enter the name of the file to create: ")
    with open(file_name, 'w') as file:
        print(f"File '{file_name}' created successfully.")

def enter_data():
    file_name = input("Enter the name of the file to enter data: ")
    with open(file_name, 'a') as file:
        while True:
            data = input("Enter data to append (or type 'done' to finish): ")
            if data.lower() == 'done':
                break
            file.write(data + '\n')
        print("Data entered successfully.")

def update_data():
    file_name = input("Enter the name of the file to update data: ")
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    print("Current data in the file:")
    for line in lines:
        print(line.strip())

    with open(file_name, 'a') as file:
        while True:
            data = input("Enter data to append (or type 'done' to finish): ")
            if data.lower() == 'done':
                break
            file.write(data + '\n')
        print("Data updated successfully.")

def print_data():
    file_name = input("Enter the name of the file to print data: ")
    try:
        with open(file_name, 'r') as file:
            print("Data in the file:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")

def delete_file():
    file_name = input("Enter the name of the file to delete: ")
    try:
        import os
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print("File not found.")

while True:
    print("\nOptions:")
    print("1. Create new file")
    print("2. Enter data in file")
    print("3. Update data in file")
    print("4. Print file data")
    print("5. Delete file")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_file()
    elif choice == '2':
        enter_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        print_data()
    elif choice == '5':
        delete_file()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

'''

This script provides a menu-driven interface where the user can choose from various options:

1. **Create new file**: Prompts the user to enter the name of the file to create.
2. **Enter data in file**: Prompts the user to enter data to append to an existing file.
3. **Update data in file**: Prompts the user to enter data to append to an existing file, displaying the current data first.
4. **Print file data**: Prompts the user to enter the name of the file and prints its content.
5. **Delete file**: Prompts the user to enter the name of the file to delete.
6. **Exit**: Exits the program.

The script handles each option accordingly, performing the specified operations on the files.
'''
