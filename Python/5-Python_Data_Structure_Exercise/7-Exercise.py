# Checks if one set is a subset or superset of another set. If found, delete all elements from that set
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print("First set", first_set)
print("Second set", second_set)

print("")

sub_set1 = first_set.issubset(second_set)
print("First set is subset of second set -", sub_set1)

sub_set2 = second_set.issubset(first_set)
print("Second set is subset of First set -", sub_set2)

print("")

sup_set1 = first_set.issuperset(second_set)
print("First set is Super set of second set -", sup_set1)

sup_set2 = second_set.issuperset(first_set)
print("Second set is Super set of First set -", sup_set2)

print("")

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)
