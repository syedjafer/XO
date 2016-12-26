
import typ_practice as tp
import os
def welcome():
	wel = open("welcome.txt")
	for line in wel:
		print line
	
	choice = input("Enter the choice : ")
#	try:
	if choice ==1:
		typ_tip()
	elif choice ==2:
		tp.practice1()
		tp.pr1()
		tp.practice2()
		tp.pr2()
		tp.practice3()
		tp.pr3()
		tp.practicealpha()
		tp.practicepara()
	elif choice ==3:
		typ_test()
	elif choice ==4:
		exit()
#	except:
#		print " please enter the prescribed key ... "


def typ_tip():
	fhand = open("tips.txt")
	for line in fhand:
		print line
	goback = raw_input("Press 'b' to go back...")
	if goback == 'b':
		os.system('clear')		
		welcome()
	






while(True):
	welcome()


















	
	
