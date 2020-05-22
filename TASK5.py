from functools import reduce
def my_func(el_x, el):
    return el_x * el
print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат вычисления всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')