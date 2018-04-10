count=0
while 1:
    print('exit 입력시 종료')
    name=input("안녕하세요. 이름을 입력하세요.")
    count+=1
    if count==1:
        print('Hi [%s]!! You are %dst person come here!' % (name,count))
    elif count==2:
        print('Hi [%s]!! You are %dnd person come here!' % (name, count))
    elif count==3:
        print('Hi [%s]!! You are %drd person come here!' % (name, count))
    elif count<11:
        print('Hi [%s]!! You are %dth person come here!' % (name, count))
    elif name=='exit':
        break
    else:
        print('Sorry [%s]. The event is closed because You are %dth person come here.'%(name,count))