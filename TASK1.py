def cash():
    mon=int(input('Введите ставку за час работы сотрудника: '))
    hou=int(input('Введите количество отработаных сотрудником часов: '))
    bon=int(input('Введите размер премии сотрудника: '))
    return (mon*hou)+bon
print(cash())