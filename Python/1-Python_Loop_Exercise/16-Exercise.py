#  Calculate the cube of all numbers from 1 to a given number
input_number = 6
for i in range(1, input_number + 1, 1):
    n = i * i * i
    print("Current Number is : {}  and the cube is {}".format(i, n))
