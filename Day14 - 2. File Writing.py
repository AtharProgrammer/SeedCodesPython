# Define the content to be written to the file
content = """This is a sample text that will be written to the file.
You can write multiple lines of text using triple quotes.
This text will be written to the file named 'example.txt'.
"""

# Open the file in write mode ('w')
with open('example.txt', 'w') as file:
    # Write the content to the file
    file.write(content)

print("Content has been written to the file successfully.")
