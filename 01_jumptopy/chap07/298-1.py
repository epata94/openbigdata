import re
p=re.compile('abc')
m = p.match("abc")
m = p.match("abcd")
m = p.match("ab")

print(m)