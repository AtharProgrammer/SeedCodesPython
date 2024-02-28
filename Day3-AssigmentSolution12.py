# Sample list with different types of elements
elements = [10, "Hello", 3.14, True, None, [1, 2, 3], {"key": "value"}, (1, 2, 3), {1, 2, 3}]

# Iterate through the list and display the type of each element
for element in elements:
    print(f"Element: {element}, Type: {type(element)}")
