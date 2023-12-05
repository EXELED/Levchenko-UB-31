import math 
x=1.825*10**2
y=18.225
z=(-3.298)*10**(-2)
a=abs((x**(y/x))-(3**math.sqrt(y/x)))
b=(y-x)*((math.cos(y-(z/(y-x))))/(1+((y-x)**2)))
s=a+b
print ('s={0:.4f}'.format (s)) 
