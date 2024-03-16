# Open the file in read mode ('r')
with open('example.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

# Modify the content
modified_content = content.replace('Hello, world!', 'Greetings!')

# Open the file in write mode ('w')
with open('example.txt', 'w') as file:
    # Write the modified content back to the file
    file.write(modified_content)

print("Data has been changed in the file successfully.")
