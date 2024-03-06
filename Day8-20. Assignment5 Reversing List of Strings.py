# Reversing List of Strings

def reverse_strings(input_list):
    return list(map(lambda s: s[::-1], input_list))

# Test the function
input_list = ['hello', 'world', 'python']
reversed_list = reverse_strings(input_list)
print(reversed_list)
