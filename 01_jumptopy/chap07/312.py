import re
p=re.compile('\section')
dest_str="\section"
# print(dest_str)
m = p.findall("\section") # not match
m = p.findall(" ection") # match

# p=re.compile('\\section')
p=re.compile(r"\section")
m = p.match("\section") # not match
print(m)