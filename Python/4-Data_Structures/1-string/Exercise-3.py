def made_string(strg):
    len1 = len(strg)
    if len1 >= 2:
        first_char = strg[0:2]
        last_char = strg[(len1 - 2):len1]
        new_str = first_char + last_char
    else:
        new_str = "Empty String"
    
    return new_str


strg = input("Enter a string: ")

result = made_string(strg)
print(result)
"""
==> OUTPUT <==
Enter a string: w3resource
~> w3ce
Enter a string: W3
~> W3W3
Enter a string: w
~> Empty String
"""
