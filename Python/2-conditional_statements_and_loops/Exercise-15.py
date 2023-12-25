import re

print("Enter a password following by this steps:\n• At least 1 letter between [a-z] and 1 letter between [A-Z].\n• At least 1 number between [0-9].\n• At least 1 character from [!@#$%&].\n• Minimum length 6 characters.\n• Maximum length 16 characters.")

s = input("Password: ")

x = True

while x:
    if (len(s) < 6 or len(s) > 16):
        if len(s) < 6:
            print("Minimum length 6 characters")
        elif len(s) > 16:
            print("Maximum length 16 characters")
        break
    elif not re.search("[a-z]", s):
        print("At least 1 letter between [a-z]")
        break
    elif not re.search("[A-Z]", s):
        print("At least 1 letter between [A-Z]")
        break
    elif not re.search("[0-9]", s):
        print("At least 1 number between [0-9]")
        print()
        break
    elif not re.search("[$#@]", s):
        print("At least 1 character from [!@#$%&]")
        break
    elif re.search("\s", s):
        break
    else:
        print("Valid Password")
        x = False
        break
if x:
    print("Not a Valid Password")
