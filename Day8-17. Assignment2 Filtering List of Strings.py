# Filtering List of Strings

def filter_strings_starting_with_A(input_list):
    return list(filter(lambda s: s.startswith('A'), input_list))

# Test the function
input_list = ['Apple', 'Banana', 'Orange', 'Apricot', 'Grapes']
filtered_list = filter_strings_starting_with_A(input_list)
print(filtered_list)
