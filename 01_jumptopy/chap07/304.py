import re
p=re.compile('[a-z]+')
m = p.match("python")   # match
m = p.match("3 python")   # not match

m = p.search("python") # match
m = p.search("3 python") # match

m = p.match("life is too short") #life만 match
m = p.search("life is too short") #life만 match
m = p.findall("life is too short") # 모든 단어가 match
print(m)

result = p.finditer("life is too short")
for r in result:
    print(r)
