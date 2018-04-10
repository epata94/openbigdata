def two_times(x):
    # if x<0:
    #     print("양수 처리만 가능합니다.")
    return x*2

# print(list(map(two_times, [1,2,3,4])))

list(map(lambda  a: a*2,[1,2,3,4]))