import win as w
import win1 as w1
import os 
import codecs
import update as up
import update1 as up1
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
for i in range(10):
	if ((count%2)==0):
		
		val = raw_input("Enter the place where do you want to insert")
		if val=='a':a = 'z'
		elif val=='b': b='z'
		elif val=='c': c='z'
		elif val=='d': d='z'
		elif val=='e': e='z'
		elif val=='f': f='z'
		elif val=='g': g='z'
		elif val=='h': h='z'
		elif val=='i': i='z'
		cont = cont.replace(val,'X')
				
		print cont
		count = count + 1
		
		if a and b and c == 'z':
			print user2+" win"
		elif a and d and g == 'z':
			print user2+" win"
		elif a and e and i == 'z':
			print user2+" win"
		elif b and e and h == 'z':
			print user2+" win"
		elif c and e and g == 'z':
			print user2+" win"
		elif c and f and i == 'z':
			print user2+" win"
		elif g and h and i == 'z':
			print user2+" win"
		elif d and e and f == 'z':
			print user2+" win"


	if count == 7:
		print "\n\t\t\t====DRAW====="
	
		
	else:
		val = raw_input("Enter the place where do you want to insert")
		if val=='a':a = 2
		elif val=='b': b='y'
		elif val=='c': c='y'
		elif val=='d': d='y'
		elif val=='e': e='y'
		elif val=='f': f='y'
		elif val=='g': g='y'
		elif val=='h': h='y'
		elif val=='i': i='y'
				
		cont =cont.replace(val,'O')
		print cont				
		count = count+1
		
		if a and b and c == 'y':
			print user1 + " win"
		elif a and d and g == 'y':
			print user1 + " win"
		elif a and e and i == 'y':
			print user1 + " win"
		elif b and e and h == 'y':
			print user1 + " win"
		elif c and e and g == 'y':
			print user1 + " win"
		elif c and f and i == 'y':
			print user1 + " win"
		elif g and h and i == 'y':
			print user1 + " win"
		elif d and e and f == 'y':
			print user1 + " win"
			
	if count == 8:
		print "\n\t\t\t========DRAW========\n"







