# Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'
print("The original string: ",str1)

new_str = "".join([i for i in str1 if i.isdigit()])

print(new_str)
