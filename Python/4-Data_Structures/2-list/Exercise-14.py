num = [7, 8, 120, 25, 44, 20, 27]

'''for i in num:
    if (i % 2) == 0:
        print(i)
    else:
        continue'''

# num = [x for x in num if x % 2 != 0]
num1 = list()
for x in num:
    if x % 2 != 0:
        num1.append(x)
    
print(num1)
"""
==> OUTPUT <==
[7, 25, 27]
"""
