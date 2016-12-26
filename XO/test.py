import codecs
cont = codecs.open('check1.py',encoding='utf-8').read()
print cont.replace('=','==')
