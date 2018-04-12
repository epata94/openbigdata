import re
p=re.compile('ca+t')
m = p.match("ct")   # not match
m = p.match("cat")  # match
m = p.match("caaat") # match

print(m)