# Write a program to find how many times substring “Emma” appears in the given string.

def how_many_time(str, st):
    count = str.count(st)
    return count


str_x = "Emma is good developer. Emma is a writer"
st = "Emma"
print("Given string", str_x)
count = how_many_time(str_x, st)
print("Emma appeared {:d} times".format(count))
