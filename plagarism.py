
l1 = ""
d={}
l = list(input())
for i in l:
	if 97<=ord(i)<=122 or 65<=ord(i)<=90:
		if i in d:
			d[i]+=1
		else:
			d[i]=1