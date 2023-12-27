def longest_word(list1):
    longest = max(list1, key=len)
    len1 = len(longest)

    print("The list:", list1)
    print("Longest word:"+ longest)
    print("Length of the longest word: {}".format(len1))


strg = input("Enter a list of words split by space: ")
list1 = strg.split()
longest_word(list1)

"""
==> OUTPUT <==
Enter a list of words split by space: Php Python C# C++ Rust Css Html Java
The list: ['Php', 'Python', 'C#', 'C++', 'Rust', 'Css', 'Html', 'Java']
Longest word:Python
~> Length of the longest word: 6
"""
