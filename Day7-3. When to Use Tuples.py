'''
When to Use Tuples
Use tuples when you have a collection of items that should not change, such as days of the week,
months of the year, or coordinates.
Tuples are often used for functions that return multiple values,as they can be unpacked easily.
'''

def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print("x:", x)  # Output: x: 10
print("y:", y)  # Output: y: 20
