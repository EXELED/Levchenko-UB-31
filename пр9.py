from random import *
x = int(input('Введите число: '))
n = int(input('Введите число: '))

def fac(n):
    if n == 0:
        return 1
    return fac(n-1)*n
print((x**n)/(fac(n)))


def st():
    a = int(input('Введите число: '))
    if a != 0:
        print(a)
        ty()
    else:
        exit()


def ty():
    a = int(input('Введите число: '))
    if a != 0:
        st()
    else:
        exit()

st()