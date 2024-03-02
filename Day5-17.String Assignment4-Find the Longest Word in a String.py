def longest_word(s):
    words = s.split()
    return max(words, key=len)

# Test the function
my_string = "Hello, beautiful world!"
print(longest_word(my_string))  # Output: "beautiful"
