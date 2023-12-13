# Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.

str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for i in temp:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        res.append(i)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
