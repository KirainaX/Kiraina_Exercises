# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent_mul(base, exp):
    mul = base
    for i in range(1, exp):
        mul = mul * base
        result = mul
    return result


base = 2
exponent = 5
print("base = {:d}\nexponent = {:d}".format(base, exponent))
result = exponent_mul(base, exponent)
print("{:d} raises to the power of {:d}: {:d}".format(base, exponent, result))
print("=======================")
base = 5
exponent = 4
print("base = {:d}\nexponent = {:d}".format(base, exponent))
result = exponent_mul(base, exponent)
print("{:d} raises to the power of {:d}: {:d}".format(base, exponent, result))
