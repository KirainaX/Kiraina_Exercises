# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False

def first_last_same(numbers=[]):
    row = len(numbers) - 1
    if numbers[0] == numbers[row]:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
result = first_last_same(numbers_x)
print("Given list:", numbers_x)
print("result is", result)
print("")
print("Given list", numbers_y)
result = first_last_same(numbers_y)
print("result is ", result)
