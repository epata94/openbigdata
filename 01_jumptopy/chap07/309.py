import re
p=re.compile('^hello\s\w')
dest_str="hello my hello world!"
m = p.findall(dest_str)
print(m)