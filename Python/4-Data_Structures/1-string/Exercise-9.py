def remove_index(strg, idx):
    first_str = strg[0:idx]
    last_str = strg[(idx + 1):]
    new_str = first_str + last_str
    return new_str
    
    
strg = input("Enter a string: ")
idx = int(input("Enter a index that u want to remove: "))
print(remove_index(strg, idx))

"""
==> OUTPUT <==
Enter a string: python
Enter a index that u want to remove: 3
~> pyton
"""
