# Iterate the given list of numbers and print only those numbers which are divisible by 5

numbers = [10, 20, 33, 46, 55]
print("Given list", numbers)
print("Divisible by 5")
for i in numbers:
    if (i % 5) != 0:
        continue
    else:
        print(i)
