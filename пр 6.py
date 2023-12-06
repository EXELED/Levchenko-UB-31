from random import randrange
N=10
a=[randrange(-10,10) for i in range(N)]
print(a, max(a), a.index(max(a))+1) 

N=10
a=[randrange(-10,10) for i in range(N)]
b=[]
for i in a:
    if i%2==1:
        b.append(i)
if len(b)==0:
    print('Нет не четных чисел')
else: 
    b.sort(reverse=True)
    print(a, b)



 