print(abs(-3))

# print(abs('-3'))
try:
    print(abs('-3'))
except TypeError as e:
    print(str(e))
print("프로그램 종료")