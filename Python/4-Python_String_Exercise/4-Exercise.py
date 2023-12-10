'''
Arrange string characters such that lowercase letters should come first
<> Given string contains a combination of the lower and upper case letters. Write a program to
arrange the characters of a string so that all lowercase letters should come first.
'''
str1 = "PyNaTive"
print('Original String:', str1)
lowerstr = []
upperstr = []
for i in str1:
    if i.islower():
        lowerstr.append(i)
    else:
        upperstr.append(i)
result = ''.join(lowerstr + upperstr)

print("Result:", result)
