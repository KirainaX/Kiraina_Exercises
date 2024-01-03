dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {}

dic3 = dic1.copy()
dic3.update(dic2)

print(dic3)
"""
==> OUTPUT <==
{1: 10, 2: 20, 3: 30, 4: 40}
"""
