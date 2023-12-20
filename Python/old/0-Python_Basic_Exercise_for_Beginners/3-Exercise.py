# Write a program to accept a string from the user and display characters that are present at an even index number.

str = input("Enter your string: ")
print("Original String is", str)
row = len(str)
for i in range(0, row, 2):
    print(str[i])
