def mul_dic(dic):
    mul = 1
    for i in dic.values():
        mul *= i
    return mul

dic = {'x': 10, 'y': 20, 'z': 30}
mul = mul_dic(dic)
print("multiply is {}".format(mul))
"""
==> OUTPUT <==
multiply is 6000
"""
