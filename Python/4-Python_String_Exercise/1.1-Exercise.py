# Write a program to create a new string made of an input string’s first, middle, and last character.

# str1 = input("Enter a string: ") 
str1 = "James"
idx = len(str1)

for i in range(0, idx, 2):
    print(str1[i], end="")
print("")