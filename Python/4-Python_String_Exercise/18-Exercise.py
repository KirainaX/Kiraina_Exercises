# Replace each special symbol with # in the following string
# import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is :", str1)

str = []

for i in str1:
    if i.isalpha():
        str.append(i)
    elif i == ' ':
        str.append(" ")
    else:
        i = '#'
        str.append(i)

new_str = ''.join(str)

'''print(new_str)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)'''

print("The strings after replacement :", new_str)
