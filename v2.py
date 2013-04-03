#Author: Ayush Mittal
#Give 2 inputs as command line argument:
#       First: The top Directory name in which you need to search
#       Second: The file name of a file which contains search query and regex patterns for files to search. See "example.txt"

import re
import os
import glob
import sys

alphabets="abcdefghijklmnopqrstuvwxyz123456789"

# Function to calculate all possible words formed by 1 substitution to given word
def substitutions1(splits):
	subs=[]
	for (a,b) in splits:
		for c in alphabets:
			if(b and c!=b[0]):
				subs.append(a+c+b[1:])
	return subs

# Function to calculate all possible words formed by 1 additions to given word
def additions1(splits):
	adds=[]
	for (a,b) in splits:
		for c in alphabets:
			adds.append(a+c+b)
	return adds

# Function to calculate all possible words formed by 1 deletion to given word
def deletions1(splits):
	dels=[]
	for (a,b) in splits:
		dels.append(a+b[1:])
	return dels

	

top_directory=sys.argv[1]	# Variable storing top directory name
querystrings=sys.argv[2]	# Variable storing file name containing query strings
f=open(querystrings,"r")	# opening query string file
list2=[]			# List2 variable
#print "query_string regular expression subdirectoryname matchedfilename"
#print "-----------------------------------------------------------------------------------------------"

# for each query given in query file
for line in f:
	line=line.split('\n')
	data2=line[0].split('\t')
	files=[]
	file_name=[]
	splits=[]
	#print data2
	for dirname, dirnames, filenames in os.walk(top_directory):
		#print data2
		if len(data2)!=2:
			continue
		temp_list=glob.glob(dirname+'/'+data2[1])
		#print data2[1]
		#print dirname+'/'+data2[1]
		
		#print temp_list
		if temp_list==[]:
			continue
		else:
			#print temp_list
			for i in temp_list:
				if os.path.isdir(i):
					continue
				files.append(i)
				#print i
				i=i.split('/')
				#print i
				file_name.append([i[-1]])
	#print file_name
	splits=[]			
	for i in range(len(data2[0])+1):
		splits.append((data2[0][:i],data2[0][i:]))
	#print splits
	poss=substitutions1(splits)+additions1(splits)+deletions1(splits)
	poss.append(data2[0])
	#print poss
	#print file_name
	for i in range(len(file_name)):
		#print file_name[i]
		a=re.split('[.]',file_name[i][0])
		#print a
		if(len(a)>2):
			file_name[i]=[a[0]]
			c=""
			for j in range(1,len(a)-1):
				c+=a[j]+'.'
			c+=a[len(a)-1]
			file_name[i].append(c)
		else:
			file_name[i]=a
	#print file_name[0]
	ans=[]
	for i in poss:
		index=0
		#print file_name
		for j in file_name:
			if i==j[0] and len(j)==2:
				sub=files[index].split(top_directory)
				sub=sub[1].split(j[0]+'.'+j[1])
				#print j[0]
				list2.append(sub[0])
				print data2[0]," ",data2[1]," ",sub[0]," ",j[0]+'.'+j[1]
			elif i==j[0]:
				#print j[0]
				sub=files[index].split(top_directory)
				sub=sub[1].split(j[0])
				list2.append(sub[0])
				print data2[0]," ",data2[1]," ",sub[0]," ",j[0]
			index=index+1	
list2.sort()
#print list2
count=1
print "subdirectoryname countofmatchedfiles"
print "--------------------------------------------------"
for i in range(len(list2)):
	if i==len(list2)-1:
		print list2[i]," ",count
		continue
	elif list2[i]!=list2[i+1]:
		print list2[i]," ",count
		count=1
	else:
		count=count+1

