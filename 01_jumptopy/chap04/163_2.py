# f =  open('F:\\python_workspace\\openbigdata\\01_jumptopy\\chap04\\새파일.txt','r')
#f =  open('새파일.txt','r')
# f =  open('.\\새파일.txt','r')
f =  open('.\\새파일_K.txt','r', encoding='UTF8')
line = f.readline()
print(line)
f.close()