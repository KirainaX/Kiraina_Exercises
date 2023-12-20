# all the function that im using it in list1

list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = [1, 2, 3, 4, 5, 6, 7]

list1.reverse() #EX1 / #EX5
list3 = [i + j for i, j in zip(list1, list2)] #EX2 / #EX5
list1.append(list2) #EX3 / #EX4 / #EX7
list1 = list(filter(None, list1)) #EX6
list1.extend() #EX8
idx = list1.index(20) #EX9
list1.remove() #EX10
