'''
Create an inner function to calculate the addition in the following way
<> Create an outer function that will accept two parameters, a and b
<> Create an inner function inside an outer function that will calculate the addition of a and b
<> At last, an outer function will add 5 into addition and return it
'''

def aceept_two(a, b):
    
    def calculate_two(a, b):
        return a + b
    
    add = calculate_two(a, b)

    return add + 5

# how to take two int like input
usr_in = input("Enter two number: ")

input_list = usr_in.split()

a = int(input_list[0])
b = int(input_list[1])

rsult = aceept_two(a, b)
print(rsult)
