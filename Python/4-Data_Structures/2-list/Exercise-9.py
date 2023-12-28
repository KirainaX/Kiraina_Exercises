my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# copy_list = my_list.copy()
copy_list = list(my_list)
# copy_list[0] = 99
print("The original list: {}".format(my_list))
print("The copy of list: {}".format(copy_list))
"""
==> OUTPUT <==
~> The original list: [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
~> The copy of list: [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
"""
