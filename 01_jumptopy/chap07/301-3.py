import re
p=re.compile('ca{2}t')
m = p.match("cat")   # not match
m = p.match("caat")   # match
m = p.match("caaaat")   #not match

p=re.compile('ca{2,5}t')
m = p.match("cat")   # not match
m = p.match("caat")   # match
m = p.match("caaaat")   #match
print(m)