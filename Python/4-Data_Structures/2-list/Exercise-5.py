my_list = ['abc', 'xyz', 'aba', '1221']
count_num = 0

for i in my_list:
    len1 = len(i)
    if len1 > 1 and i[0] == i[len1 - 1]:
        count_num += 1
    else:
        pass
print("Result : {}".format(count_num))
"""
==> OUTPUT <==
~> Result : 2
"""
