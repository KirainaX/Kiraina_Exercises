tuplex = 5, 10, 15, 20, 25
print("The original tuple:", tuplex)

tuplex = tuplex + (30,)
print("Tuple after adding number:", tuplex)

tuplex = tuplex[:3] + (35, 40, 45) + tuplex[:3]
print("Tuple ofter munipilachion:", tuplex)

listx = list(tuplex)

listx.append(80)

tuplex = tuple(listx)

print("adding a number to tuple by list:",tuplex)
"""
==> OUTPUT <==
The original tuple: (5, 10, 15, 20, 25)
Tuple after adding number: (5, 10, 15, 20, 25, 30)
Tuple ofter munipilachion: (5, 10, 15, 35, 40, 45, 5, 10, 15)
adding a number to tuple by list: (5, 10, 15, 35, 40, 45, 5, 10, 15, 80)
"""
