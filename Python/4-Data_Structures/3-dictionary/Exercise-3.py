dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}

new_dic = {}

'''new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)'''

for i in (dic1, dic2, dic3):
    new_dic.update(i)

print(new_dic)
"""
==> OUTPUT <==
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
