# Count the total number of digits in a number
n = 75869
count = 0
while n != 0:
    n = n // 10
    count = count + 1
print(count)
