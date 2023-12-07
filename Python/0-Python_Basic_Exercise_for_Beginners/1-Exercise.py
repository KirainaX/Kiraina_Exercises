'''
Calculate the multiplication and sum of two numbers.
Given two integer numbers, return their product only if the product is equal
to or lower than 1000. Otherwise, return their sum.
'''

def add_mul(a, b):
    res = a * b
    if res <= 1000:
        return res
    else:
        return a + b

a = 20
b = 30
result = add_mul(a, b)
print("number1 ",a)
print("number1 ",b)
print("The result is ", result)
print("=====================================")
c = 40
d = 30
result = add_mul(c, d)
print("number1 ",c)
print("number1 ",d)
print("The result is ", result)
