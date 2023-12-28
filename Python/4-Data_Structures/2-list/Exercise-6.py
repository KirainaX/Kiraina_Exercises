def last(n):
    return n[-1]

def sorted_list(my_list):
    return sorted(my_list, key=last)


my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sort_list = sorted_list(my_list)
print(sort_list)
"""
==> OUTPUT <==
~> [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
