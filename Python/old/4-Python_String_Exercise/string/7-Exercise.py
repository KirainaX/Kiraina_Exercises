# tring characters balance Test
'''
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if
all the characters in the s1 are present in s2. The character’s position doesn’t matter.
'''

def balance_string(s1, s2):
    flag = True
    for i in s1:
        if i in s2:
            continue
        else:
            flag = False

    return flag
            

s1 = "Yn"
s2 = "PYnative"

result = balance_string(s1, s2)
print("s1 and s2 are balanced:",result)

s1 = "Ynf"
s2 = "PYnative"

result = balance_string(s1, s2)
print("s1 and s2 are balanced:",result)
