# Prompt the user to input employee data
employee_data = []
while True:
    name = input("Enter employee name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    age = input("Enter employee age: ")
    department = input("Enter employee department: ")
    # Store the employee data as a tuple
    employee_data.append((name, age, department))

# Define the path to the text file
file_path = 'employee_data.txt'

# Write the employee data to the text file
with open(file_path, 'w') as file:
    for employee in employee_data:
        file.write(f"Name: {employee[0]}, Age: {employee[1]}, Department: {employee[2]}\n")

print("Employee data has been stored in 'employee_data.txt' successfully.")
