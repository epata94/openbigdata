while True:
    print('프로그래밍이 왜 좋으세요?')
    reason=input('종료 입력시 프로그램 종료')

    if reason == '종료':
        break
    name = input('이름을 입력해주세요.')
    print('설문에 응답해 주셔서 감사합니다.')
    try:
        f = open('D:\Python_workspace\jump_to_python\python_jaryo\practice/poll.txt','r')
        #f = open('D:\\1\pycharm\python_jaryo\practice/poll.txt','r')
        f.close()
        f = open('D:\Python_workspace\jump_to_python\python_jaryo\practice/poll.txt', 'a')
        #f = open('D:\\1\pycharm\python_jaryo\practice/poll.txt','a')
        a=f.write('[%s] %s'%(name,reason))
        a=f.write('\n')
        print('[%s] %s'%(name,reason))
        f.close()
    except:
        print('poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.')
        case=int(input('1. 종료\n2. 변경된 파일 경로 입력\n'))
        if case==1:
            print('종료합니다.')
            break
        elif case==2:
            path=input('변경된 파일 경로를 입력하세요. :')
            f2 = open(path, 'a')

            if reason == '종료':
                f2.close()
                break
            else:
                a = f2.write('[%s] %s' % (name, reason))
                a = f2.write('\n')
                print('[%s] %s' % (name, reason))
                f2.close()



