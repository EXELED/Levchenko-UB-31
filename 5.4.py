s=input()
c=''
d=0
for i in range(len(s)):
	if s[i]=="а":
		c+="о"
		d+=1
	else:
		c+=s[i]
print(c)
print("в строке",len(s), "символов")
print("звмен",d)
		
