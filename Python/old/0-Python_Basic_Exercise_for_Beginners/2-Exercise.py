# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

print("Printing current and previous number sum in a range(10)")
j = 0
for i in range(10):
    result = i + j
    print("Current Number {:d} Previous Number  {:d}  Sum:  {:d}".format(i, j, result))
    j = i
