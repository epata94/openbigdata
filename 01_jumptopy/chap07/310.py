import re
p=re.compile('^python\s\w+',re.MULTILINE)
dest_str="""python one python debug
life is too shrot
python two
you need python
python three
"""
m = p.findall(dest_str)
print(m)