'''
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
A recursive function is a function that calls itself again and again.
'''

def recursive():
    j = 0
    for i in range(11):
        result = i + j
        j = result

    print(result)


recursive()
