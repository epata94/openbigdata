while True:
    print('프로그래밍이 왜 좋으세요?')
    reason=input('종료 입력시 프로그램 종료')

    if reason == '종료':
        break
    name = input('이름을 입력해주세요.')
    print('설문에 응답해 주셔서 감사합니다.')
    f=open('D:\Python_workspace\jump_to_python\python_jaryo\practice/poll.txt','a')
    #f = open('D:\\1\pycharm\python_jaryo\practice/poll.txt', 'a')
    a=f.write('[%s] %s'%(name,reason))
    a=f.write('\n')
    print('[%s] %s'%(name,reason))
    f.close()