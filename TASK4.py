list1 = [1, 2, 4, 2, 5, 3, 5, 10, 9 ,10, 33, 5, 11, 13, 11, 73]
list2 = [i for i in list1 if list1.count(i) < 2]
print(list2)