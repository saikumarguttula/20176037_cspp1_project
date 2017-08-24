def lcs(str1, str2):
    r = ""
    global len1, len2
    len1, len2 = len(str1), len(str2)
    for i in range(len1):
        for j in range(len2):
            sum=0
            match=""
            while ((i+sum < len1) and (j+sum<len2) and str1[i+sum] == str2[j+sum]):
                match += str2[j+sum]
                sum+=1
            if (len(match) > len(r)):
                r = match
    return r

list1 = []
import os
for file in os.listdir():
	if file.endswith(".txt"):
		x = os.path.join(file)
		list1.append(x)
print(list1)

import re
words1=[]
for i in range(len(list1)):
	file = open(list1[i], 'r')
	text = file.read()
	file.close()
	text = re.sub('[^a-zA-Z0-9\ \']+', " ", text)
	text = text.replace(" ","")
	words = list(text.split())
	words1.append(words)
# print(words)
# print(words1)
list3 = []
for i in range(len(words1)):
	list2 =[]
	for j in range(len(words1)):
		r= lcs(" ".join(str(x) for x in words1[i])," ".join(str(x) for x in words1[j]))
		t_length = len1 + len2
		fnl_r = ((len(r) * 2) / t_length) * 100
		list2.append(fnl_r)
	list3.append(list2)
for i in range(len(list3)):
	print(list3[i])