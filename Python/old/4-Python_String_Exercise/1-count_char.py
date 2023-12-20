# Write a Python program to count the number of characters (character frequency) in a string.
def count_char(str1):
     new_str = {}
     for i in str1:
          if i in new_str:
               new_str[i] += 1
          else:
               new_str[i] = 1
     return new_str
        

str1 = "google.com"

result = count_char(str1)
print(result)

"""
==> OUTPUT <==
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""