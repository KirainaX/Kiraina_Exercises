# Remove and add item in a list
list1 = [34, 54, 67, 89, 11, 43, 94]
print("Original list", list1)

rmv_list = list1.pop(4)
print("List After removing element at index 4", list1)
list1.insert(2, 11)
print("List after Adding element at index 2", list1)
list1.append(11)
print("List after Adding element at last", list1)
