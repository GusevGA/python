list2 = [int(i) for i in input('Введите значения списка через пробел: ').split()]
i = 0
while True:
    if i >= len(list2) - 1:
        break
    list2[i], list2[i + 1] = list2[i + 1], list2[i]
    i = i + 2
print(f'Ваш список: {list2}')
