list1 = []

for i in range(100, 401):
    s = str(i)

    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        list1.append(s)

print(','.join(list1))
print("")
