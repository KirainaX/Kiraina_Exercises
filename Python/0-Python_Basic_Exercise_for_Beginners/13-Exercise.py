# Print multiplication table from 1 to 10
for i in range(1, 11):
    print(i, end=" ")
    for j in range(2, 11):
        if i >= 2:
            j = i * j
            print(j, end=" ")
        else:
            print(j, end=" ")
    print("")