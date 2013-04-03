import os
import glob
import sys
a=sys.argv[1] #TopDirectory
fin=sys.argv[2]
f=open(fin,'r')
p1=0
p2=0
def insertion(w,s):
	p1,p2=0,0
	if len(w)+1!=len(s):
		return 0
	else:
		for x in s:
			if s[0:p1]+s[p1+1:]==w:
				return 1
			p1=p1+1
		return 0

def subs(w,s):
	p1,p2=0,0
	if len(w)!=len(s):
		return 0
	else:
		for x in s:
			if s[p1]!=w[p1]:
				p2=p2+1
			p1=p1+1
		if p2==1:
			return 1
		else:
			return 0

index=0
s1=[]
list2=[]
print "query_string regular expression subdirectoryname matchedfilename"
print "-----------------------------------------------------------------------------------------------"
for line in f:
	array=[] #stores full name
	barray=[] #stores file name
	splitted=[] #stores splitted name
	line=line.split('\n')
	line=line[0]
	f1=line
	f1=f1.split('\t')
	if len(f1)!=2:
		continue
	fi=f1[0]
	query=f1[1]
	for dirname, dirnames, filenames in os.walk(a):
		store=glob.glob(dirname+'/'+query)
		print store
		if store==[]:
			continue
		else:
			for w in store:
				if os.path.isdir(w):
					continue
				array.append(w)
				x=w.split('/')
				y=x[-1]
				z=y.split('.')
				splitted.append(z[0])
				barray.append(y)
				index=0
		for w in splitted:
			if w==fi:
				s1=array[index].split(a)
				s1=s1[1]
				s1=s1.split(barray[index])
				list2.append(s1[0])
				print fi," ",query," ",s1[0]," ",barray[index]
			elif insertion(w,fi)==1:
				s1=array[index].split(a)
				s1=s1[1]
				s1=s1.split(barray[index])
				list2.append(s1[0])
				print fi," ",query," ",s1[0]," ",barray[index]
			elif insertion(fi,w)==1:
				s1=array[index].split(a)
				s1=s1[1]
				s1=s1.split(barray[index])
				list2.append(s1[0])
				print fi," ",query," ",s1[0]," ",barray[index]
			elif subs(w,fi)==1:
				s1=array[index].split(a)
				s1=s1[1]
				s1=s1.split(barray[index])
				list2.append(s1[0])
				print fi," ",query," ",s1[0]," ",barray[index]
		index=index+1
		#print list2
list2.sort()
index=1
counter=1
print "subdirectoryname countofmatchedfiles"
print "--------------------------------------------------"
list2.append("!@#$%^&**")
for line in range(0,len(list2)-1,1):
	if list2[line]!=list2[line+1]:
		print list2[line]," ",counter
		counter=1
	else:
		counter=counter+1
