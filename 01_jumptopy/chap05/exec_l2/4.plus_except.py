def two_sum(a,b):
    sum=a+b
    return sum
while 1:
    list=input('두 수를 입력하세요.:').split()
    if '종료' in list:
        print('프로그램을 종료합니다.')
        break
    try:
        int(list[0])
    except:
        print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요. '%(1,list[0]))
        continue
    try:
        a=int(list[0])
        b=int(list[1])
        print(two_sum(a,b))
    except:
        print('%d번째 입력이 [%s]입니다. 숫자를 입력하세요. '%(2,list[1]))
# IndexError # ValueError

