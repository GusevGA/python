revenue=int(input('Введите выручку: '))
costs=int(input('Введите издержки: '))
if revenue>costs:
    print('Предприятие работает на прибыль')
    profit= revenue - costs
    profitmargin=profit/revenue*100
    print('Рентабельность выручки составляет ',profitmargin,'%')
    worker=int(input('Введите количество сотрудников: '))
    workercash=profit//worker
    print('Прибыль фирмы в расчете на одного сотрудника составляет:', workercash)
else:
    print('Предприятие работает в убыток')