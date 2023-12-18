# Write a Python program to calculate the length of a string.
def count_string(str1):
    count = 0
    
    for i in str1:
        count += 1

    return count

str1 = input("Enter a string: ")
print(count_string(str1))

"""
==> output <==
Enter a string: Zakaria
7
"""