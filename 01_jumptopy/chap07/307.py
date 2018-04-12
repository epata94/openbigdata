import re
p=re.compile('[a-z]+')
# m = p.match("python")   # match
m = p.search("3 python")   # match

print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())