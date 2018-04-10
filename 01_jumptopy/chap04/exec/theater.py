
while 1:
    print('나이를 입력하세요:')
    age=int(input('-1을 입력하면 종료됩니다.'))
    if age==-1:
        break
    elif age<3:#공짜
        print('공짜')
    elif age>=3 and age<13: #10달러
        print('10달러')
    elif age>=13:#15달러
        print('15달러')