list1 = [1, 10, 15, 18, 25, 37, 40, 73]

generator = (el for el in list1 if el > el-1)
for i in generator:
    print(i)