# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

str_list1 = []

print("Original list of string")
print(str_list)

for i in str_list:
    if i == "":
        continue
    else:
        str_list1.append(i)

# str_list1 = list(filter(None, str_list))

print("After removing empyt strings")
print(str_list1)
