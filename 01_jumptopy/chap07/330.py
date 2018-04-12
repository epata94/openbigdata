import re
p=re.compile('a.b')
m = p.match("akb")
m = p.match("a1b")
m = p.match("a$b")

p=re.compile('330.py')
m = p.match("330.py") # match
m = p.match("330_py") # match / 원하는 결과가 아님
p=re.compile('330[.]py')
m = p.match("330.py") # match
m = p.match("330_py") # not match / 원하는 결과

print(m)