# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

char = 0
digit = 0
symbol = 0

for i in str1:
    if i.isalpha():
        char = char + 1
    elif i.isdigit():
        digit = digit + 1
    else:
        symbol = symbol + 1

print("Total counts of chars, digits, and symbols in this string", str1)

print("Chars = ", char)
print("Digits = ", digit)
print("Symbol = ", symbol)
