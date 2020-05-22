from itertools import count
from itertools import cycle

def my_count(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def my_cycle(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
my_count(start_number = int(input("Введите первое число: ")), stop_number = int(input("Введите последнее число: ")))
my_cycle(my_list = [1, 2, 3], iteration = int(input("Введите количество повторений: ")))