s=input()
d=''
for i in range(len(s)//2):
	if s[i]=='п':
		d+='.Звездочка.'
	else:
		d+=s[i]
print(d)
		
