x=int(input('Введите значение числа числа x: '))
y=int(input('Введите значение числа числа y: '))
def my_func(x, y):
    return 1/x ** abs(y)
print(my_func(x, y))