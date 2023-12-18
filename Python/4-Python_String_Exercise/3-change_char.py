'''
Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
'''

def change_char(str1):

    '''first_char = str1[0]
    for i in str1:
        if str1[0] == first_char:
            new_str = ''.join([str1[0]])
        elif i != first_char:
            new_str = ''.join(i)
        


    return new_str'''
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    return str1
        



str1 = "restart"
result = change_char(str1)
print(result)

"""
==> OUTPUT <==
Sample String : 'restart'
Expected Result : 'resta$t'
"""
