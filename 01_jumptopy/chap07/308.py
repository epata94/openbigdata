import re
p=re.compile('aaa.bbb')
# dest_str="aaa|bbb"
dest_str="""aaa
bbb"""
m = p.match(dest_str) # not match

p=re.compile('aaa.bbb',re.DOTALL)
m = p.match(dest_str) # match
print(m)

p=re.compile('[a-z]+',re.I)
m= p.match('python') #match
m =p.match('Python') #match
m = p.match('PYTHON') #match
print(m)
