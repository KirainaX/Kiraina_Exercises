str1 = input("Input a word to reverse: ")
# str1 = "Zakaria"
# rev_str = ''.join(reversed(str1))
# print(rev_str)
for i in range(len(str1) - 1, -1, -1):
    print(str1[i], end="")
print("")
