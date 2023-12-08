# Write a program to take three names as input from a user in the single input() function call.
names = []
num = int(input("Enter how many names u will enter: "))
print("Enter three string Emma Jessa Kelly")
for i in range(num):
    print("Name: ", end="")
    itm = input()
    names.append(itm)

for i in names:
    for j in range(1, num + 1):
        print("Name",j,": ",i)
