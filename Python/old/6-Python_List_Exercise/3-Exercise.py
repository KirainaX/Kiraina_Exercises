# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

numbers = [1, 2, 3, 4, 5, 6, 7]

square_list = list()

for i in numbers:
    j = i ** 2
    square_list.append(j)

print(square_list)
