from random import *
a=[]
n=8
for i in range(n):
    b = []
    for j in range(n):
        b.append(randint(0,n))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
    
first=sum(a[0])
b = 0

for k in a:
    if sum(k) != first:
        b += 1
        break

for k in range(n):
    if sum([o[k] for o in a]) != first:
        b += 1
        break

if b == 0:
    print('Матрица является магическим квадратом')
else:print('Матрица не является магическим квадратом')



a=[]
n=7
m=9
for i in range(n):
    b = list()
    for j in range(m):
        b.append(randint(n,m))
    a.append(b)

for i in range(n):
    for j in range(m):
        print(a[i][j],end = ' ')
    print()

for i in a:
    i[0],i[n] = i[n],i[0]

print('___')

for i in range(n):
    for j in range(m):
        print(a[i][j],end = ' ')
    print()