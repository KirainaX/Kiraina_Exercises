bouth = []

for i in range(1500, 2701):
    if ((i % 7) == 0) and ((i % 5) == 0):
        bouth.append(i)
    else:
        continue
        
for i in bouth:
    print("{},".format(i), end="")
print("")
