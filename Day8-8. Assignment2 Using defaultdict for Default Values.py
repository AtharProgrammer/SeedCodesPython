from collections import defaultdict

# Using defaultdict to specify default value type
fruit_counts = defaultdict(int)
fruit_counts["apple"] += 1
fruit_counts["banana"] += 2
print("Fruit counts:", dict(fruit_counts))  # Output: {'apple': 1, 'banana': 2}
