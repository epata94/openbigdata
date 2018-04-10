store_ = []
def address():
    try:
        f = open("C:\python\poll.txt", 'r')
    except FileNotFoundError as t:
        t = print("poll.txt 파일이 없습니다. 아래 중 선택하세요")
        print(t)
        print("1. 종료")
        print("2. 변경된 파일 경로 입력")
        select_ = int(input(":"))
        if select_ == 1:
            print("종료되었습니다")
        elif select_ == 2:
            address_ = str(input("변경된 파일 경로를 입력하세요. :"))
            address_fix = (address_ + "\\"+ "poll.txt")
            return address_fix


def interesting():
    while True:
        print("프로그래밍이 왜 좋으세요?")
        answer_ = input(str(":"))
        if answer_ == "종료":
            break
        store_.append(answer_)
        print("이름을 입력해주세요")
        if answer_ == "종료":
            break
        name_ = input(str(":"))
        print("응답해주셔서 감사합니다")
        store_.append(name_)
        f.write("[" + name_ + "]")
        f.write(" " + answer_ + "\n")
        continue
    f.close()

address_value = address()
while True:
    try:
        f = open(address_value, 'a')
        interesting()
        break
    except TypeError as type_error:
        type_error = "다시 실행해주십시요"
        print(type_error)
        break
