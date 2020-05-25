file_obj = open('003.txt', 'r')
employees = {}
for line in file_obj:
    person, value = line.split()
    employees[person] = value
    if int(value) < 20000:
        print(f'{person } Зарплата ниже 20000')
file_obj.close()