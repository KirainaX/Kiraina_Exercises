def common_element(list1, lilst2):
    result = False
    for i in list1:
        if i in list2:
            result = True
            return result
    return result
    

list1 = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
list2 = [19, 20, 39, 29, 19, 59, 69, 49, 89, 59, 49]
#list1 = [1, 2, 3, 4, 5]
#list2 = [6, 7, 8, 9]
result = common_element(list1, list2)
print(result)
"""
==> OUTPUT <==
~> True
"""