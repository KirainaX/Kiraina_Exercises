def change_char(strg):
    len1 = len(strg)
    first_char = strg[len1 - len1]
    last_char = strg[len1 -1]
    new_str = last_char + strg[(len1-len1) + 1 : (len1 - 1)] + first_char
    return new_str


strg = input("Enter a string: ")
result = change_char(strg)
print(result)

"""
==> OUTPUT <==
Enter a string: Python
~> nythoP
"""
