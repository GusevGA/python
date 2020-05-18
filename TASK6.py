def int_func(text):
    return text.title()
def my_title(text):
    text_1 = list(text)
    text_1[0] = text_1[0].upper()
    return ''.join(text_1)
my_list1 = []
for word in input('Введите слова разделяя их пробелами: ').split(' '):
    my_list1.append(int_func(word))
print(f'Вы ввели: {" ".join(my_list1)}')