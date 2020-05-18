a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
def my_func(a, b, c):
    x = [a, b, c]
    x.remove(min(a, b, c))
    return sum(x)
print('Сумма максимальных чисел:', my_func(a, b, c))