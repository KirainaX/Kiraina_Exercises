strg = input("Enter a string: ")
list1 = {}
for i in strg:
    if i in list1:
        list1[i] += 1
    else:
        list1[i] = 1

print(list1)

"""
==> OUTPUT <==
Enter a string: google.com
~> {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""
