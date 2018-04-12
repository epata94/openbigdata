import re
p=re.compile('.+[.]...')
# m = p.match("a.txt")        # match
# m = p.match("bk3.py")       # not match
m = p.match("python.doc")   # match
m = p.match(".doc")   # match

print(m)