list1 = ['Зима', 'Весна', 'Лето', 'Осень']
dict1 = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите номер месяца, от 1 до 12: "))
if month ==1 or month == 12 or month == 2:
        print('Время года', dict1.get(1))
        print('Время года', list1[0])
elif month == 3 or month == 4 or month ==5:
    print('Время года', dict1.get(2))
    print('Время года', list1[1])
elif month == 6 or month == 7 or month == 8:
    print('Время года', dict1.get(3))
    print('Время года', list1[2])

elif month == 9 or month == 10 or month == 11:
    print('Время года', dict1.get(4))
    print('Время года', list1[3])
else:
        print("Введите цифру от 1 до 12.")