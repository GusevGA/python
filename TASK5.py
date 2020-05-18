def my_sum(a):
    a = a.split()
    b = []
    for i in a:
        b.append(int(i))
    return sum(b)
x = 0
while 1:
    a = input('Введите цифры через пробел: ')
    if a == 'q':
        break
    x += my_sum(a)
    print('Сумма введенных чисел равна: ', x)