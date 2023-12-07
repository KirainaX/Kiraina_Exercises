# Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chr(str, n):
    new_str = str[n:]
    return new_str


strg = input("Enter your string: ")
n = int(input("Enter the index of the character you want to remove: "))

remove = remove_chr(strg, n)
print(remove)
