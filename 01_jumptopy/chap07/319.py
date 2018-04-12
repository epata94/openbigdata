import re
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())
#p = re.compile(r'(\b\w+)\s+\2') #<-- Error
print(p.findall('Paris in the the spring kkk kkk OK'))