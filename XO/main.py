import os 
import codecs
import check as c
import check1 as c1
a=''
b=''
c=''
d=''
e=''
f=''
g=''
h=''
i=''
cont = codecs.open('xo.txt',encoding='utf-8').read()
user1 = raw_input("Enter the user1 name : ")
user2 = raw_input("Enter the user2 name : ")
print (" user 1 will start ultimately")
fhand = open("xo.txt")
info = fhand.readlines()
os.system('xdg-open "xo.txt"')
count = 1
for i in range(9):
	if ((count%2)==0):
		
		val = raw_input("Enter the place where do you want to insert")
		#c.check(val)
		cont = cont.replace(val,'X')
				
		print cont
		count = count + 1
		#if (a=b=c | a=d=g | a=e=i | b=e=h |c=e=g| c=f=i |g=h=i |d=e=f):
		#	print user1 , " WINS"

		
	else:
		#res = O
		val = raw_input("Enter the place where do you want to insert")
		#c1.check1(val)		
		cont =cont.replace(val,'O')
		print cont				
		count = count+1
		#if (a=b=c | a=d=g | a=e=i | b=e=h |c=e=g| c=f=i |g=h=i |d=e=f):
		#	print main.user2 , " WINS"

	
	#elif:print"DRAW......" 


#c.fin()
#c1.fin()











