def not_poor(strg):
    snot = strg.find('not')
    spoor = strg.find('poor')

    if spoor > snot and spoor > 0 and snot > 0:
        strg = strg.replace(strg[snot: (spoor + 4)], "good")
        return strg
    else:
        return strg


strg = input("Enter a string: ")
print(not_poor(strg))

"""
==> OUTPUT <==
Enter a string: The lyrics is not that poor!
~> The lyrics is good!
Enter a string: The lyrics is poor!
~> The lyrics is poor!
"""
