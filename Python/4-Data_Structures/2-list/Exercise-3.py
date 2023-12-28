my_list = [1, 100, 1000,2934]

'''max_num = max(my_list)
print("The largest number is {}".format(max_num))'''

max = my_list[0]
for i in my_list:
    if i > max:
        max = i
print("The largest number is {}".format(max))
"""
==> OUTPUT <==
~> The largest number is 2934
"""
