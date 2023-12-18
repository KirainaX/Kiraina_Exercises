# Create a mixed String using the following rules
'''
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any
leftover chars go at the end of the result.
'''
def mix_string(s1, s2):

    len1 = len(s1)
    len2 = len(s2)

    mid1 = int(len1 / 2)
    mid2 = int(len2 / 2)

    first = s1[mid1 - 1 : mid1] + s2[mid2 + 1]
    middle = s1[mid1 : mid1 + 1] + s2[mid2 : mid2 + 1]
    last = s1[len1 - 1] + s2[mid2 - 1]

    s3 = first + middle + last
    print(s3)




s1 = "Abc"
s2 = "Def"

mix_string(s1, s2)
