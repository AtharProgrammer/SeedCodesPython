import tkinter as tk
from tkinter import messagebox
import pyodbc

server = 'LAPTOP-PG47J1NE'
database = 'DemoDatabase'

# Use trusted connection for Windows Authentication
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = conn.cursor()

# Function to sign up a user
def signup():
    username = username_entry.get()
    password = password_entry.get()
    
    try:
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User signed up successfully!")
    except pyodbc.Error as e:
        conn.rollback()
        messagebox.showerror("Error", f"Error occurred: {e}")

# Create main window
root = tk.Tk()
root.title("User Authentication")

# Create signup page
signup_frame = tk.Frame(root)
signup_frame.pack(padx=20, pady=20)

tk.Label(signup_frame, text="Username:").grid(row=0, column=0, sticky="e")
username_entry = tk.Entry(signup_frame)
username_entry.grid(row=0, column=1)

tk.Label(signup_frame, text="Password:").grid(row=1, column=0, sticky="e")
password_entry = tk.Entry(signup_frame, show="*")
password_entry.grid(row=1, column=1)

signup_button = tk.Button(signup_frame, text="Sign Up", command=signup)
signup_button.grid(row=2, columnspan=2, pady=10)


root.mainloop()

# Close the database connection when the application is closed
conn.close()
