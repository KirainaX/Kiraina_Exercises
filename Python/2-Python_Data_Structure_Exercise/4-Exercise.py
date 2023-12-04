# Count the occurrence of each element from a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

elm_count = {}
for i in sample_list:
    if i in elm_count:
        elm_count[i] += 1
    else:
        elm_count[i] = 1
print(f"Element count of each item ", elm_count)
