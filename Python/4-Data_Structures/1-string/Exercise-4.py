def replace_chr(strg):
    first_chr = strg[0]
    replace = strg.replace(first_chr, "$")

    new_str = first_chr + replace[1:]

    return new_str


strg = input("Enter a string: ")

result = replace_chr(strg)
print(result)
"""
==> OUTPUT <==
Enter a string: restart
~> resta$t
"""
