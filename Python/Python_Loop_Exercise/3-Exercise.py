# Calculate the sum of all numbers from 1 to a given number
sum = 0
n = int(input("Enter number : "))
for i in range(1, n + 1):
    sum = sum + i
print("sum is : {}".format(sum))
