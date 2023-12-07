# pattern 5
nbr = int(input("Enter number: "))
for i in range(1, nbr):
    for j in range(1, i + 1):
        j = i
        print(j,end=" ")
    print("")
