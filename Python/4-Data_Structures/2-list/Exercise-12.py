def remove_elements(color, num_element):
    new_list = []
    for i in num_element:
        new_list.append(color[i])
    for i in new_list:
        color.remove(i)
    
    return color


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
num_element = [0, 4, 5]
result = remove_elements(color, num_element)
print(result)
"""
==> OUTPUT <==
['Green', 'White', 'Black']
"""