# Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Sample list", sample_list)

list_sample = list()
for i in sample_list:
    if i not in list_sample:
        list_sample.append(i)
print("Uniqui items", list_sample)

tuple_list = tuple(list_sample)
print("Tuple", tuple_list)

print("Min:", min(tuple_list))
print("Max:", max(tuple_list))
