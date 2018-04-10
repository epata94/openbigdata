import time

print(time.time())

print(time.localtime(time.time()))
my_time = time.localtime(time.time())
# my_time.tm_year
# print("안녕하세요. 현재 시각은 %d년 %d월 %d일 %시 %분 %초입니다."%(my_time.tm_year,my_time.tm_mon,my_time.tm_mday, my_time.tm_hour, my_time.tm_min, my_time.tm_sec))
print("안녕하세요. 현재 시각은 %d년 %d월 "%(my_time.tm_year,my_time.tm_mon))

print(time.asctime(time.localtime(time.time())))
print(time.ctime())

print(time.strftime('%x',time.localtime(time.time())))
print(time.strftime('%c',time.localtime(time.time())))

print("프로그램 종료")
