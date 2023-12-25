list1 = []
binary = []
num = input("Enter a sequence of comma separated 4 digit binary numbers : ")
binary = num.split(',')

for i in binary:
    a = int(i, 2)

    if not a % 5:
        list1.append(i)

print(''.join(list1))
