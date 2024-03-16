# Specify the source and destination file paths
source_file_path = 'source_file.txt'
destination_file_path = 'destination_file.txt'

# Open the source file in read mode ('r')
with open(source_file_path, 'r') as source_file:
    # Read the content from the source file
    content = source_file.read()

# Open the destination file in write mode ('w')
with open(destination_file_path, 'w') as destination_file:
    # Write the content to the destination file
    destination_file.write(content)

print("Data from source file has been written to the destination file successfully.")
