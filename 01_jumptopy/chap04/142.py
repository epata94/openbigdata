def my_sum(num1, num2):
    print("덧셈 연산")
    internal_result = num1+num2
    if internal_result > 0:
        print("연산 결과가 +로 분석됩니다.")
    elif internal_result == 0:
        print("연산 결과가 0으로 분석됩니다.")
    else:
        print("연산 결과가 -로 분석됩니다.")
    return num1+num2

result = my_sum(1,2)
result = my_sum(3,4)
result = my_sum(5,6)
result = my_sum(7,8)
result = my_sum(9,10)

print("최종 연산 결과: "+result)
print("계산기 ver1.0 종료")
