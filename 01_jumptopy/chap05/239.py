from copy import copy
from copy import deepcopy

a=3
print(id(3))
print(id(a))
b=a
print(id(b))
c= copy(a)
print(id(c))

d= deepcopy(a)
print("deep copy")
print(d)
print(id(d))

a=4
print(a)
print(b)
print(c)


l1=[1,2,3]
l2=l1
l3=copy(l1)
print(id(l1))
print(id(l2))
print(id(l3))
