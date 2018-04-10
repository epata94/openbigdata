def compare(num):
    if num==1 or num==0:
        Referee='아닙니다.'
    else:
        if num%10==0:
            return True
        else:
            return False

while 1:
    print('-1 to quit')
    num=int(input('정수를 입력하시오'))
    if num==-1:
        print('종료')
        break
    Referee=compare(num)
    if Referee==True:
        print('%d는 10의 배수가 맞습니다'%num)
    else:
        print('%d는 10의 배수가 아닙니다' % num)
