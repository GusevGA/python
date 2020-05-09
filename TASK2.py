sec= int(input('введите количество секунд: '))
hou= sec//3600
min= (sec-hou*3600)//60
sec= sec%60
print(hou,'час',min,'мин',sec,'сек')