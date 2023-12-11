# Calculate the sum and average of the digits present in a string
'''
Given a string s1, write a program to return the sum and average of the digits that appear in the
string, ignoring all other characters.
'''
str1 = "PYnative29@#8496"
result = 0
count = 0
for i in str1:
    if i.isdigit():
        result += int(i)
        count += 1

final = result / count

print("Sum is:", result, "Average is", final)
