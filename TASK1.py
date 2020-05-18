a=int(input('Введите значение числа a: '))
b=int(input('Введите значение числа b: '))
def numbers(a, b):
    try:
        return a // b
    except ZeroDivisionError as e:
        print(f'Делить на ноль не хочешь ты!')
answer=numbers(a, b)
print(answer)