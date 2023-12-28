my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)
        
print(new_list)
"""
==> OUTPUT <==
~> [10, 20, 30, 50, 60, 40, 80]
"""
