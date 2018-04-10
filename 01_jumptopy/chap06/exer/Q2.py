list_num=input('범위, 첫번째 수, 두번째 수를 입력하세요.(종료: 프로그램 종료): ').split()
list_num[0]=int(list_num[0])
list_num[1]=int(list_num[1])
list_num[2]=int(list_num[2])
first_multiple_list=[]
second_multiple_list=[]
for i in range(1,list_num[0]+1):
    if i%(list_num[1])==0:
        first_multiple_list.append(i)
    if i%(list_num[2])==0:
        second_multiple_list.append(i)
first_multiple_list=set(first_multiple_list)
second_multiple_list=set(second_multiple_list)

merged_multiple_list=first_multiple_list|second_multiple_list
result=0

for multiple_number in merged_multiple_list:
    result=result + multiple_number

print('0부터 %d 까지의 범위를 선택하셨습니다. 이 중에서'%list_num[0])
print('%d의 배수는 %s입니다.'%(list_num[1],first_multiple_list))
print('%d의 배수는 %s입니다.'%(list_num[2],second_multiple_list))
print('%d과(와) %d의 배수는 %s입니다.'%(list_num[1],list_num[2],merged_multiple_list))
print('따라서 0부터 %d 이하의 범위내에서 %d와 %d의 배수의 총합은 %d입니다.'%(list_num[0],list_num[1],list_num[2],result))