# Print the following pattern
#n = int(input("Enter numbers of * : "))
n = 5
for i in range(n):
    for j in range(i + 1):
        print("*",end=" ")
    print("")
for i in range(n - 1, 0, -1):
    for r in range(i, 0 , -1):
        print("*", end=" ")
    print("")
    