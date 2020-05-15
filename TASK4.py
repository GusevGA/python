num= int(input('ведите целое положительное число: '))
maxnum=0
while num>0:
    x=num%10
    if x>=maxnum: maxnum=x
    num=num//10
print(maxnum)
