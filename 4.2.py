A=input()
B=input()
 
if A<B: 
    for i in range(A, B+1):
        print(i)
else:
    for i in reversed(range(B, A+1)):
        print(i)