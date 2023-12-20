#  Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l1 = l1[1:6:2]
l2 = l2[::2]
l3 = l1 + l2
print("Element at odd-index positions from list one")
print(l1)
print("Element at even-index positions from list two")
print(l2)
print("Printing Final third list")
print(l3)
