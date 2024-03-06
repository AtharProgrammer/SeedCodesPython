#Finding Maximum Value in List of Dictionaries

def find_max_value_dict(input_list):
    return max(input_list, key=lambda d: d['value'])

# Test the function
input_list = [{'value': 10}, {'value': 25}, {'value': 15}, {'value': 20}]
max_value_dict = find_max_value_dict(input_list)
print(max_value_dict)
