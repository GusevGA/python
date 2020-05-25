f_obj= open('005.txt', 'w')
numbers=[int(i) for i in input('Введите числа через пробел: ').split()]
summa = sum(numbers)
print(summa)
f_obj.writelines(f'{summa}')
f_obj.close()