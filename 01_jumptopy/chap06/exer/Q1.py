# def convert_input(dan):
#     try:
#         dan = int(dan)
#         return dan
#     except ValueError as e:
#         print(str(e))

while True:
    dan=input('\n숫자를 입력하세요(-1:종료, all:구구단 전체 출력): ')
    if dan == 'all':
        for i in range(2, 10):
            for j in range(1, 10):
                print('%d * %d = %d' % (i, j, i * j))
            print()
            Flag=1
    elif dan == '-1':
        break

    try:
        dan=int(dan)

        for i in range(1,10):
            print('%d * %d = %d' % (dan, i, dan * i))
    except ValueError as e:
        print(e)