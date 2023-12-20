# Accept a list of 5 float numbers as an input from the user

numbers = []

for i in range(1, 6):
    print("Enter number at location {:d}: ".format(i), end="")
    num = float(input())
    numbers.append(num)

print("User List:", numbers)
