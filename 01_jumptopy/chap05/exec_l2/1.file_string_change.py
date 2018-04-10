f=open('D:\Python_workspace\jump_to_python\python_jaryo\practice/learning_python.txt','r')
a=f.read()
print(a)
f.close()

f=open('D:\Python_workspace\jump_to_python\python_jaryo\practice/learning_python_copyed.txt','w')
# a=f.read()
f.write(a.replace('python','C'))
print(a.replace('python','C'))
f.close()

