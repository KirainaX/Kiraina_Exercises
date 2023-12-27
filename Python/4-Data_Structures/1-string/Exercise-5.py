def swap_char(str1, str2):
    first_str1 = str1[0:2]
    first_str2 = str2[0:2]

    new_str1 = first_str2 + str1[2:]
    new_str2 = first_str1 + str2[2:]

    print("Result: {} , {}".format(new_str1, new_str2))


str1 = input("Enter a first string: ")
str2 = input("Enter a second string: ")

swap_char(str1, str2)
"""
==> OUTPUT <==
Enter a first string: abc
Enter a second string: xyz
~> Result: xyc , abz
"""
