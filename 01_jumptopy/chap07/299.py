import re
p=re.compile('[a-zA-Z]')
# m = p.match("glob")
m = p.match("able")
m = p.match("Able")


# p=re.compile('[0-9]')
# m = p.match("a9") # not match
# m = p.match("9a") # match
# m = p.match("9 kfjlsjflsk sdfsdlfj") # match


print(m)