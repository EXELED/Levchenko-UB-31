n=int(input('введите натуральное число'))
a=1
b=1
for i in range(2, n+1):
	b*=i
	a+=b
print(b)
