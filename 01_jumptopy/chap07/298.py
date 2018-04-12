import re
p=re.compile('[abc]')
# m = p.match("a")
# m = p.match("before")
# m = p.match("dude")
m = p.match("glob")

print(m)