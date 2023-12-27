def change_str(strg):
    end_1st, end_2st = "ing", "ly"
    len1 = len(strg)
    if len1 < 3:
        new_str = strg
    elif strg[(len1 - 3):] == end_1st:
        new_str = strg + end_2st
    else:
        new_str = strg + end_1st
        
    return new_str


strg = input("Enter a string: ")
result = change_str(strg)
print(result)
"""
==> OUTPUT <==
Enter a string: abc
~> abcing
Enter a string: string
~> stringly
Enter a string: WE
~> WE
"""
