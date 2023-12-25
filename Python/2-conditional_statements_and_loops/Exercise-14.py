s = input("Enter a string: ")
count_alpha = 0
count_digit = 0
for i in s:
    if i.isalpha():
        count_alpha += 1
    elif i.isdigit():
        count_digit += 1
    else:
        pass
print("Letters {}".format(count_alpha))
print("Digits {}".format(count_digit))
