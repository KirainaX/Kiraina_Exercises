# Write a program to take three names as input from a user in the single input() function call.
names = []
j = 0
row = 1
num = int(input("Enter how many names u will enter: "))
idx = num
for i in range(1, num + 1):
    print("Name{:d}: ".format(i), end="")
    itm = input()
    names.append(itm)

print("Enter three string ",end="")
for i in names:
    print(i, end=" ")
print("")

print("====================================", names)
for i in names:
    for j in range(row, num - idx + 2):
        print("Name{:d}: ".format(j), i)
        idx = idx + 1
        row = row + 1

'''str1, str2, str3 = input("Enter three string ").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)'''
