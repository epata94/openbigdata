class Restaurant :

    def __init__(self, input_name, input_cusine_type) :
        self.name = input_name
        self.cusine_type = input_cusine_type
        self.todays_customer = 0
        self.total_customer_mng = open("고객서빙현황관리로그.txt", 'r')
        self.number_served = int(self.total_customer_mng.readline())
        self.total_customer_mng.close()
        self.total_customer_mng = open("고객서빙현황관리로그.txt", 'w')
    def __del__(self):
        print("%s 레스토랑 문닫습니다." % self.name)
        self.total_customer_mng.write(str(self.todays_customer + self.number_served) + '\n')
        self.total_customer_mng.close()
        print("\n이용해 주셔서 감사합니다.\n")

    def describe_restaurant(self) :
        print("\n저희 레스토랑 명칭은 %s이고 %s 전문점입니다." %(self.name, self.cusine_type))

    def open_restaurant(self) :
        print("\n저희 %s 레스토랑이 오픈했습니다." %self.name)

    def reset_number_served(self) :
        self.todays_customer = 0
        print("\n손님 카운팅을 0으로 초기화 하였습니다.")

    def increment_number_served(self, input_customer) :
        self.todays_customer += input_customer
        print("손님 %d명 들어오셨습니다. 자리를 안내해 드리겠습니다." %input_customer)

    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다." %(self.todays_customer+self.number_served))

input_name, input_cusine_type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split(' ')

First_restaurant = Restaurant(input_name, input_cusine_type)
First_restaurant.describe_restaurant()

open_close = input("레스토랑을 오픈하시겠습니까? (y/n) ")
if open_close == "y" :
    First_restaurant.open_restaurant()
    while 1 :
        input_customer = input("\n어서오세요. 몇명이십니까?(초기화:0입력,종료:-1,누적고객 확인:p) : ")
        if input_customer == "-1" : break
        elif input_customer == '0' : First_restaurant.reset_number_served()
        elif input_customer == 'p' : First_restaurant.check_customer_number()
        else :
            First_restaurant.increment_number_served(int(input_customer))

