my_list = [100, 10, 1000,2934]
min_lst = my_list[0]

for i in my_list:
    if i < min_lst:
        min_lst = i
print("The smallest number in the list is {}".format(min_lst))
"""
==> OUTPUT <==
~> The smallest number in the list is 10
"""