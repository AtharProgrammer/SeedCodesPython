def are_anagrams(s1, s2):
    print(sorted(s1))
    print(sorted(s2))
    return sorted(s1) == sorted(s2)

# Test the function
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True
