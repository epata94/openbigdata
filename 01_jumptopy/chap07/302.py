import re
p=re.compile('ab?c')
m = p.match("abc")   # match
m = p.match("ac")   # match

print(m)