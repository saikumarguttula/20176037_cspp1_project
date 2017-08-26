class stringmatching():
	def lcs(self,str1, str2):
	    r = ""
	    global len1, len2
	    len1, len2 = len(str1), len(str2)
	    for i in range(len1):									#checking largest common string
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
	if file.endswith(".txt"):									#Searches for files which are in .txt format
		x = os.path.join(file)									#joins each txt file to our path
		list1.append(x)											#used to kept all the text files in the list
# print(list1)

import re
words1=[]
for i in range(len(list1)):
	file = open(list1[i], 'r')									#Opens the text files one by one
	text = file.read()											#Reads the sentences from text document
	file.close()												#Closes the file
	text = re.sub('[^a-zA-Z0-9\ \']+', " ", text)				#Allows lower, upper case letters and numbers to pass
	text = text.replace(" ","")									#removes spaces
	words = list(text.split())									#converts each string to list of strings
	words1.append(words)						
# print(words)
# print(words1)
list3 = []
for i in range(len(words1)):
	list2 =[]
	for j in range(len(words1)):
		s = stringmatching()									#creating object for the class
		r= s.lcs(" ".join(str(x) for x in words1[i])," ".join(str(x) for x in words1[j]))												#calling the function lcs 
		t_length = len1 + len2
		fnl_r = ((len(r) * 2) / t_length) * 100
		list2.append(fnl_r)
	list3.append(list2)
	
for i in range(len(list3)):										#printing in matrix pattern
	print(list3[i])