import tkinter as tk
from tkinter import messagebox
import pyodbc

server = 'LAPTOP-PG47J1NE'
database = 'DemoDatabase'

# Use trusted connection for Windows Authentication
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = conn.cursor()


# Function to create a new employee
def create_employee():
    name = name_entry.get()
    age = age_entry.get()
    designation = designation_entry.get()
    
    try:
        cursor.execute("INSERT INTO Employees (Name, Age, Designation) VALUES (?, ?, ?)", (name, age, designation))
        conn.commit()
        messagebox.showinfo("Success", "Employee added successfully!")
        clear_entries()
    except pyodbc.Error as e:
        conn.rollback()
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to read all employees
def read_employees():
    try:
        cursor.execute("SELECT * FROM Employees")
        employees = cursor.fetchall()
        display_text.delete('1.0', tk.END)
        for employee in employees:
            display_text.insert(tk.END, f"ID: {employee[0]}, Name: {employee[1]}, Age: {employee[2]}, Designation: {employee[3]}\n")
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to update an employee
def update_employee():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    designation = designation_entry.get()
    
    try:
        cursor.execute("UPDATE Employees SET Name=?, Age=?, Designation=? WHERE ID=?", (name, age, designation, id))
        conn.commit()
        messagebox.showinfo("Success", "Employee updated successfully!")
        clear_entries()
    except pyodbc.Error as e:
        conn.rollback()
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to delete an employee
def delete_employee():
    id = id_entry.get()
    
    try:
        cursor.execute("DELETE FROM Employees WHERE ID=?", (id,))
        conn.commit()
        messagebox.showinfo("Success", "Employee deleted successfully!")
        clear_entries()
    except pyodbc.Error as e:
        conn.rollback()
        messagebox.showerror("Error", f"Error occurred: {e}")

# Function to clear entry fields
def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    designation_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Employee Management System")

# Create entry fields
id_label = tk.Label(root, text="ID:")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

designation_label = tk.Label(root, text="Designation:")
designation_label.grid(row=3, column=0)
designation_entry = tk.Entry(root)
designation_entry.grid(row=3, column=1)

# Create buttons for CRUD operations
create_button = tk.Button(root, text="Create", command=create_employee)
create_button.grid(row=4, column=0)

read_button = tk.Button(root, text="Read", command=read_employees)
read_button.grid(row=4, column=1)

update_button = tk.Button(root, text="Update", command=update_employee)
update_button.grid(row=4, column=2)

delete_button = tk.Button(root, text="Delete", command=delete_employee)
delete_button.grid(row=4, column=3)

# Text widget to display employee details
display_text = tk.Text(root, height=10, width=50)
display_text.grid(row=5, columnspan=4)

root.mainloop()

# Close the database connection when the application is closed
conn.close()
