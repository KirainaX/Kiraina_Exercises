# Write a Program to extract each digit from an integer in the reverse order.
'''For example, If the given int is 7536, the output shall be “6 3 5 7“,
with a space separating the digits.'''
number = int(input("Enter a number: "))
# number = 7536
# revers = 0
while number > 0:
    rem = number % 10
    # revers = (revers * 10) + rem
    number = number // 10
    print(rem, end=" ")
print("")
