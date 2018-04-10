save_path='.'
file_name='\\poll.txt'

def read_content():
    f = open(save_path+file_name,'r', encoding='UTF8')
    opinions = f.readlines()

    print("< 현재 누적 응답 현황 >")
    for opinion in opinions:
        print(opinion,end='')
    print('')
    f.close()

while True:
    try:
        read_content()
    except:
        print('기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.')
        case=int(input('1. 종료 2.새로운 파일 생성 3. 변경된 파일 경로 입력: '))
        if case==1:
            print('종료합니다.')
        elif case==2:
            pass
        elif case==3:
            new_path=input('변경된 파일 경로를 입력하세요. :')
            save_path = new_path
            read_content()

    reason=input('프로그램이 왜 좋으세요? ("종료" 입력시 프로그램 종료) : ')

    if reason == '종료':
        f.close()
        break
    name = input('이름을 입력해주세요: ')
    print('설문에 응답해 주셔서 감사합니다.\n')

    f = open(save_path+file_name, 'a',encoding='UTF8')
    f.write('[%s] %s' % (name, reason))
    f.write('\n')
    f.close()

