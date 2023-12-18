# Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

def mix_string(s1, s2):
    first = s1[0] + s2[0]

    mid1 = int(len(s1) / 2)
    mid2 = int(len(s2) / 2)

    middle = s1[mid1:mid1 + 1] + s2[mid2:mid2 + 1]

    len1 = len(s1)
    len2 = len(s2)

    last = s1[len1 - 1] + s2[len2 - 1]
    
    s3 = first + middle + last
    print("Mix String is ", s3)


s1 = "Zakaria"
s2 = "Bouzrida"
mix_string(s1, s2)

'''def mix_string(s1, s2):
    # get first character from both string
    first_char = s1[0] + s2[0]

    # get middle character from both string
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

    # get last character from both string
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
    res = first_char + middle_char + last_char
    print("Mix String is ", res)


s1 = "Zakaria"
s2 = "Bouzrida"
mix_string(s1, s2)'''
