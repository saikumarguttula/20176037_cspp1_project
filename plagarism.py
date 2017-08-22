def dictionary(l,m):
	global d1,d2
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
	return d1,d2

def numerator(l,m):
	global dot
	dot = 0
	for i in d1:
		for j in d2:
			if i == j:
				dot = dot + (d1[i]*d2[j])
	return dot

def denominator(d1,d2):
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

def answer(dot,k):
	cos = (dot/(k)) * 100
	return cos

list0 = []
import os
for file in os.listdir():
	if file.endswith(".txt"):
		x = os.path.join(file)
		list0.append(x)
print(list0)

import re
sent1 = []
for i in range(len(list0)):
	file = open(list0[i],'r')
	text = file.read().lower()
	file.close()
	text = re.sub('[^a-z\ \']+'," ",text)
	sent = list(text.split())
	sent1.append(sent)
print((sent1))
sent2 = []

for i in range(len(sent1)):
	for j in range(i,len(sent1)-1):
		d1,d2= dictionary(sent1[i],sent1[j+1])
		dot = numerator(d1,d2)
		k = denominator(d1,d2)
		cos = answer(dot,k)
		sent2.append(cos)
print(sent2)