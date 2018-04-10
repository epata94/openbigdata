def compare(num1,num2,num3):
    temp1=[num1,]
    temp2=[num2,]
    for i in range(1,num3):
        temp1.append(num1*i)
        temp2.append(num2*i)
    s1=set(temp1)
    s2=set(temp2)
    s3= s1 & s2
    print(s3)
    if num3 in s3:
        return True
    else:
        return False
    #print(temp1)
    #print(temp2)
list_a=[]

while 1:
    print('3개의 양수를 입력하세요')
    print('-1 to quit')
    list_a=input().split()

    size=len(list_a)
    if size==3:
        num1=int(list_a[0])
        num2=int(list_a[1])
        num3=int(list_a[2])

        if num1<0 or num2<0 or num3<0:
            print('비정상적인 값 입력(0 미만의 값은 넣을 수 없습니다.)')
            continue
        elif compare(num1, num2, num3) == True:
            print('%d은(는) %d와(과) %d의 공배수입니다' % (num3, num1, num2))
        else:
            print('%d은(는) %d와(과) %d의 공배수가 아닙니다.' % (num3, num1, num2))
    elif size==2:
        print('정상적인 입력이 아닙니다.')
        continue
    elif size==1:
        print('정상적인 입력이 아닙니다!')
        if int(list_a[0])==-1:
            print('-1이 입력되었으므로 종료됩니다.')
            break
    #if num1%num3==0 and num2%num3==0


'''
    배수를 어디까지 구할 것인가?
    num3까지 하면 되겠지.
    num1이나 num2를 2로 곱하면 배수들이 나온다.
    리스트를 만들어서 num1과 num2의 공배수를 추려내자.
    공배수 중에 num3이 있는지 확인하면 끝.
'''