def remove_duplicates(s):
    seen = set()
    result = ''
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

# Test the function
my_string = "hello"
print(remove_duplicates(my_string))  # Output: "helo"
