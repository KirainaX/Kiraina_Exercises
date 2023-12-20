'''
Write a Python program to get a string made of the first 2 and last 2 characters
of a given string. If the string length is less than 2, return the empty string instead.
'''
def first_last(str1):
    len1 = len(str1)
    if len1 > 1:
        two_first = str1[0:2]
        two_last = str1[len1 - 2:len1]

        new_str = two_first + two_last
    else:
        return "Empty String"

    return new_str

str1 = "w3resource"
result = first_last(str1)
print(result)
print("===")
str1 = "w3"
result = first_last(str1)
print(result)
print("===")
str1 = "w"
result = first_last(str1)
print(result)
print("===")

"""
==> OUTPUT <==
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""