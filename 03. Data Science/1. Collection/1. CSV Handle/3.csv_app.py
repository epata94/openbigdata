import csv
import math

menu = """
<CSV Handle 연습예제>
0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬
메뉴를 선택하세요: """

def get_csv_row_instance(primary_key):
    Row_instance=[]
    row_index=0
    NotFound=True
    for i in range(len(data)):
        if primary_key in data[i]:
            row_index=i
            NotFound=False
            break
        else:
            NotFound=True

    for row in data[row_index]:
        if NotFound==True:
            print("Not Found '%s'"%primary_key)
            break
        Row_instance.append(row)
    return Row_instance

def get_csv_col_instance(col_name):
    col_instance=[]
    col_index=data[0].index(col_name)

    for col in data[1:]:
        col_instance.append(col[col_index])
    return col_instance

def Convert_Type(col_instance):
    try:
        col_instance = list(map(int, col_instance))
    except ValueError:
        col_instance = list(map(float, col_instance))

    return col_instance

def My_Sum(data_list):
    My_Sum=0
    for i in range(len(data_list)):
        My_Sum+=data_list[i]
    return My_Sum

def My_Average(data_list):
    My_Average=My_Sum(data_list)
    My_Average/=len(data_list)
    return My_Average

def My_Max(data_list):
    My_Max=0
    for i in range(len(data_list)):
        if My_Max<data_list[i]:
            My_Max=data_list[i]
    return My_Max

def My_Min(data_list):
    My_Min=min(data_list)
    return My_Min

def My_Deviation(data_list):
    My_Deviation=0
    Average=My_Average(data_list)
    space="\t\t"
    print("표본\t\t편차")
    for i in range(len(data_list)):
        My_Deviation=data_list[i]-Average
        print(str(data_list[i])+space+str(My_Deviation))

def My_Standard_Deviation(data_list):# 표준편차
    Variance=My_Variance(data_list)
    My_Standard_Deviation=math.sqrt(Variance)
    return My_Standard_Deviation

def My_Variance(data_list):#분산
    My_Variance=0
    Average=My_Average(data_list)

    for i in range(len(data_list)):# 제곱 **
        My_Variance+=((data_list[i])-Average)**2
    My_Variance/=len(data_list)
    return My_Variance

def My_Ascendant(data_list):#오름차순
    data_list.sort()
    for i in range(len(data_list)):
        print("%g "%data_list[i],end="")
    print()

def My_Descendant(data_list):#내림차순
    data_list.sort(reverse=True)
    for i in data_list:
        print("%g "%i,end="")
    print()

def print_row(row_instance):
    for row_element in row_instance:
        print("%s "%row_element,end="")
    print()

def print_col(col_instance):
    for col_element in col_instance:
        print(col_element)

with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data=list(csv.reader(infile))


while True:
    case=int(input(menu))
    if case==0:
        print('프로그램을 종료합니다.')
        break
    Access_key = input('Access Key를 입력하세요: ')

    if case==1:#행 (Row)
        print('행 데이터는 아래와 같습니다.')
        print_row(get_csv_row_instance(Access_key))
    elif case==2:#열 (Col)
        print('열 데이터는 아래와 같습니다.')
        print_col(get_csv_col_instance(Access_key))
    elif case == 3:  # 합
        print_col(get_csv_col_instance(Access_key))
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        print("총합: %s"%My_Sum(col_data))
    elif case == 4:  # 평균값
        print_col(get_csv_col_instance(Access_key))
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        print("평균값: %s"%My_Average(col_data))
    elif case == 5:  # 최대값
        print_col(get_csv_col_instance(Access_key))
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        print("최대값: %s"%My_Max(col_data))
    elif case == 6:  # 최소값
        print_col(get_csv_col_instance(Access_key))
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        print("최소값: %s"%My_Min(col_data))
    elif case == 7:  # 편차
        print('편차(Deviation) 공식 : 표본값 - 평균')
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        My_Deviation(col_data)
    elif case == 8:  # 표준편차
        print_col(get_csv_col_instance(Access_key))
        print("표준편차(Standard Deviation) 공식: √분산")
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        print("표준편차: %s"%My_Standard_Deviation(col_data))

    elif case == 9:  # 분산
        print_col(get_csv_col_instance(Access_key))
        print('분산(Variance) 공식: ∑(표본-평균)**2/표본수')#**== 제곱
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        print(My_Variance(col_data))
    elif case == 10: # 오름차순 정렬
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        My_Ascendant(col_data)
    elif case == 11: # 내림차순 정렬
        col_data=Convert_Type(get_csv_col_instance(Access_key))
        My_Descendant(col_data)
    else:
        print('유효하지 않은 값 입력')