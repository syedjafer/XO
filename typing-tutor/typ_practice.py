
#this is the first excersise....
import difflib
import os
import time

def practice1():
	fe = '\n\n\nasdfgh ;lkjhj asdfgf ;lkjhj asdfgf ;lkjhj asdfgf ;lkjhj\n\n\n'
	print fe
#	result = raw_input("Enter the above statement : ")
#practice1()




def pr1():
	fe = '\n\n\nasdfgh ;lkjhj asdfgf ;lkjhj asdfgf ;lkjhj asdfgf ;lkjhj\n\n\n'
	result = raw_input("Enter the above statement : ")
	if result == fe :
		print "Excellent"
		fhand = open('firstex.txt')
		for line in fhand:
			print line
	
	else :
		print "Try again : "
		practice1()
		#pr1()




#this is the second excercise




def practice2():
	se = '\n\n\nawerqfa  ;oiupi; awerqfa ;oiupj; awerqfa ;oiupi;\n\n\n'
	print se
#practice2()

def pr2():
	result = raw_input("Enter the above statement : ")
	se = 'awerqfa  ;oiupi; awerqfa ;oiupj; awerqfa ;oiupi;'
	if result == se:
		print "Excellent"
		fhand = open('secodex.txt')
		for line in fhand:
			print line
		tr = raw_input()
	else:
		print "Try again : "
		practice2()
		#pr2()

#this is the third excersice

def practice3():
	te = "gftftrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj"
	print te
#practice3()

def pr3():
	result = raw_input("Enter the  above statement : ")
	te = "gftftrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj"
	if result == te:
		print "Excellent"
		fhand = open('thirdex.txt')#create 
		for line in fhand:
			print line
		tr = raw_input()
	else : 
		print "Try again"
		practice3()
		#pr3()



def practicealpha():
	fhand = open ("alpha.txt")#create
	for line in fhand:
		print line
	print "\n\n\nPrint the above lines for fingering practice ....."
	fnew = open("tryalpha.txt",'w+')
	print " type in the promt window and save it ....."	
	
	#fnew.write(new)
	
	os.system('xdg-open "tryalpha.txt"')
	new = raw_input("after finishing press enter")
	diff = difflib.ndiff(open('tryalpha.txt').readlines(),open("alpha.txt").readlines())
	try:
		while 1:
			print diff.next()
	except:
		pass


def practicepara():
	fhand = open("para.txt")#create
	for line in fhand:
		print line
	print "\n\n\n Print the above lines ....."
	fnew1= open("trypara.txt","w+")
	print " type in the prompt window and save it "
	os.system('xdg-open "trypara.txt"')	
	new1 = raw_input("after finishing press enter")
	#fnew1.write(new1)
	diff = difflib.ndiff(open('trypara.txt').readlines(),open("para.txt").readlines())
	try:
		while 1:
			print diff.next()
	except:
		pass



#practicealpha()
#practicepara()
	
	
