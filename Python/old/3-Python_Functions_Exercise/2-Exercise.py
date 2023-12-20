# Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    print("Printing values")
    for i in args:
        print(i)


# call function with 3 arguments
func1(20, 40, 60)
print("\n")
# call function with 2 arguments
func1(80, 100)
