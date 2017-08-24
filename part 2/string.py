lst = []
import os
for file in os.listdir():
	if file.endswith(".txt"):
		x = os.path.join(file)
		# print(type(x))
		lst.append(x)
print(lst)

import re
words = []
for i in range(len(lst)):
	file = open(lst[i],'r')
	text = file.read().lower()
	file.close()
	text = re.sub('[^a-z\ \']+'," ",text)
	sent = list(text.split())
	words.append(sent)
print((words))
m = []
answer = ""
len1, len2 = len(string1), len(string2)
for i in range(len1):
	for j in range(len2):
		lcssum=0
		match=''
	while ((i+lcssum < len1) and (j+lcssum<len2) and string1[i+lcssum] == string2[j+lcssum]):
	    match += string2[j+lcssum]
        lcssum+=1
	if (len(match) > len(answer)):
		answer = match

