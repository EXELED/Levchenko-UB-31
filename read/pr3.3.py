a=input('Введите число')
b=[]
c=[]
for i in a:
	if int(i)%2==0:
		b.append(i)
	else:
		c.append(i)
print('Введенное число',a)
print('четные цыфры',b)
print('не четные цыфры',c)