my_list =[]
while True:
    info = input('Enter the user information: ')
    if info == '':
        break

    else:
        newinfo = info + '\n'
        my_list.append(newinfo)
        f_obj= open('001.txt', 'w')
        f_obj.writelines(my_list)
        f_obj.close()