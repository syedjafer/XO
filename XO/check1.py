import main
def check1(val):
	a=''
	b=''
	c=''
	d=''
	e=''
	f=''
	g=''
	h=''
	i=''
	if val == 'a': a='O'
	elif val== 'b': b='O'
	elif val == 'c': c = 'O'
	elif val == 'd':d='O'
	elif val == 'e':e='O'
	elif val == 'f':f='O'
	elif val == 'g': g='O'
	elif val == 'i': i = 'O'
	
#def fin1():
	if (a==b==c=='O' or  a==d==g=='O' or  a==e==i=='O' or b==e==h=='O' or c==e==g=='O' or  c==f==i=='O' or g==h==i=='O' or d==e==f=='O'):
		print main.user1 , " WINS"
		
