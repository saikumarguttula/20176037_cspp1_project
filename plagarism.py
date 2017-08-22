file = open('text1.txt', 'r')
s1 = list(file.read().split())
file = open('text2.txt', 'r')
s2 = list(file.read().split())
def lower(s1,s2):
	global l,m
	l,m = [],[]
	for i in (s1):
		k = i.lower()
		l.append(k)
	for i in (s2):
		k = i.lower()
		m.append(k)
	return l,m
lower(s1,s2)
def numerator(l,m):
	global d1,d2,dot
	d1,d2 = {},{}
	for i in l:
		if i in d1:
			d1[i] = d1[i] + 1
		else:
			d1[i]=1

	for i in m:
		if i in d2:
			d2[i] = d2[i] + 1
		else:
			d2[i]=1
	dot = 0
	for i in d1:
		for j in d2:
			if i == j:
				dot = dot + (d1[i]*d2[j])
	return dot
numerator(l,m)
def denominator(dot):
	l1 = d1.values()
	l2 = d2.values()
	l1,l2 = list(l1),list(l2) 
	sum = 0
	for i in l1:
		sum = sum + (i * i)
	answer = sum ** (1/2)
	sum = 0
	for i in l2:
		sum = sum + (i * i)
	answer1 = sum ** (1/2)
	global k
	k = answer * answer1
	return k
denominator(dot)
cos = (dot/(k)) * 100
print(str(cos) + " % matching")