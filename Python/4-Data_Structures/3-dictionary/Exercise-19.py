d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
    if k1 == k2:
        d3[k1] = v1 + v2
    else:
        d3[k1] = v1
        d3[k2] = v2

print(d3)
"""
==> OUTPUT <==
{'a': 400, 'b': 400, 'c': 300, 'd': 400}
"""
