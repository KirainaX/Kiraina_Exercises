s = input("Enter a string: ")
n = int(input("Enter the number you want to find words longer than the number you entered: "))
s_list = s.split()
new_list = []

for i in s_list:
    len1 = len(i)
    if len1 > n:
        new_list.append(i)
    else:
        continue
print("the words in the string that u have enter that longer than {} is {}".format(n, new_list))
"""
==> OUTPUT <==
Enter a string: The quick brown fox jumps over the lazy dog
Enter the number you want to find words longer than the number you entered: 3
the words in the string that u have enter that longer than 3 is ['quick', 'brown', 'jumps', 'over', 'lazy']
"""
