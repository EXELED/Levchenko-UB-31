N=int(input('Введите число'))
fib0=0
fib1=1
fib=0
i=0
while i<N:
	fib=fib0+fib1
	print(fib)
	fib0=fib1
	fib1=fib
	i=i+1
