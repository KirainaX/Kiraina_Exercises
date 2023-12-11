# Write a program to count occurrences of all characters within a string

str1 = "Apple"

char_dict = dict()

for i in str1:
    count = str1.count(i)
    char_dict[i] = count

print("Result:", char_dict)
