#Sorting Dictionary by Values

def sort_dict_by_values(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))

# Test the function
input_dict = {'apple': 5, 'banana': 3, 'orange': 7}
sorted_dict = sort_dict_by_values(input_dict)
print(sorted_dict)
