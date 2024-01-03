def remove_key(dic, key):
    if key in dic:
        del dic[key]
    
    return dic


dic = {'x': 10, 'y': 20, 'z': 30}
print("dictionary after remove a key:\n{}".format(remove_key(dic, 'x')))
"""
==> OUTPUT <==
{'y': 20, 'z': 30}
"""
