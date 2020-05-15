my_list = [7, 5, 3, 3, 2]
print(f'Список рейтинга {my_list}')
my_list.append(int(input('Добавьте значение рейтига: ')))
print(f'тОбновленный рейтинг:{sorted(my_list, reverse=True)}')