import re
p=re.compile('Crow|Servo')
m = p.match('Crow') #match
m = p.match('Servo') #match
print(m)

p=re.compile('short$')
m = p.search('Life is too short')
print(m) #match
