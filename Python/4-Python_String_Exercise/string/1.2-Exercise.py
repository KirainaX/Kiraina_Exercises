# Write a program to create a new string made of the middle three characters of an input string.


# mine
str1 = "Zakaria"
# str1 = "JhonDipPeta"
len = len(str1)
mid = int(len / 2) - 1
for i in range(mid, len):
    if i == (mid + 3):
        break
    else:
        print(str1[i], end="")
print("")

# ==============================================
'''def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("ZakariaBouzrida")
get_middle_three_chars("Zakaria")'''
