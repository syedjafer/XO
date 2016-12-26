import main
def check(val):
	a=''
	b=''
	c=''
	d=''
	e=''
	f=''
	g=''
	h=''
	i=''
	if val == 'a': a='X'
	elif val== 'b': b='X'
	elif val == 'c': c = 'X'
	elif val == 'd':d='X'
	elif val == 'e':e='X'
	elif val == 'f':f='X'
	elif val == 'g': g='X'
	elif val == 'i': i = 'X'
def fin():	
	if (a==b==c=='X' or  a==d==g=='X' or a==e==i=='X' or b==e==h=='X' or c==e==g=='X' or c==f==i=='X'  or g==h==i=='X' or d==e==f=='X'):
		print main.user2 , " WINS"	
