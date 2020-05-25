my_list = []
file_obj = open('002.txt', 'r')
lines = 0
words = 0
for line in file_obj:
    lines += line.count("\n")
    words = len(set(open('002.txt').read().split()))
    print(f'Количество слов в строке {words}')
    print(f'Номер строки:  {lines}')
file_obj.close()