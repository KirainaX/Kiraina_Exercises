# Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
def append_middle(s1, s2):
    print("Original Strings are", s1, s2)

    mid = int(len(s1) / 2)

    s3 = s1[:mid] + s2 + s1[mid:]
    print("After appending new string in middle:", s3)


append_middle("Ault", "Kelly")
