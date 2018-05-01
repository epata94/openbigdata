print("Start")
import urllib.request
from pandas import DataFrame
import datetime
import time
import os
import xml.etree.ElementTree as ET

file_limit=3 #디렉터리 하나에 들어갈 수 있는 파일 수 제한
result = [] #결과값을 저장하는 리스트

if not os.path.isdir("CSV_test"): #CSV_test 디렉터리가 현재 경로에 없으면
    os.mkdir('CSV_test') #CSV_test 디렉터리를 생성

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1') #매장명
    store_sido = element.findtext('aname2') #매장 시
    store_gungu = element.findtext('aname3') #매장 군/구
    store_address = element.findtext('aname5') #매장 주소

try:
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])
    #매장명,시,군/구,주소를 리스트에 추가
    cnt = 0 #디렉터리에 저장된 파일의 갯수
    dir_num = 1 #파일을 저장하고 있는 디렉터리의 갯수
    if not os.path.isdir('CSV_test\\test%d' %dir_num):
        os.mkdir('CSV_test\\test%d' %dir_num)
    # CSV_test아래에 csv파일을 저장할 디렉터리가 없다면 생성하고 번호를 붙여준다.
    nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))
    #데이터프레임 생성, result=리스트에 저장된 데이터, columns=리스트에 저장된 데이터의 형식
    f=open('CSV_test\index.txt','r')
    data = f.read()
    cnt = int(data)
    f.close()
    #CSV_test폴더 아래에 index.txt파일에서 현재 파일 갯수를 읽어온다.
except:
    f=open('CSV_test\index.txt','w')
    data = f.write(str(cnt))
    f.close()
    #CSV_test폴더 아래에 index.txt파일이 없다면 파일을 만들고 현재 파일의 갯수 써준다.
try:
    f=open('CSV_test\dir_index.txt','r')
    data = f.read()
    dir_num=int(data)
    f.close()
    #CSV_test폴더 아래에 dir_index.txt파일에서 파일을 저장하고 있는 디렉토리의 번호를 읽어온다.
except:
    f=open('CSV_test\dir_index.txt','w')
    data= f.write(str(dir_num))
    f.close()
    #CSV_test폴더 아래에 dir_index.txt파일이 없다면 파일을 만들고 파일을 저장하고 있는 디렉토리의 번호를 읽어온다.
now = datetime.datetime.now()
dateNow=now.strftime('%Y-%m-%d')
timeNow=dateNow+'_'+time.strftime('%H%M%S')
#파일의 이름을 연-월-일_시분초.csv로 생성한다.
while True:
    dir_name='CSV_test\\test'+str(dir_num)+'\\' #dir_name은 test에 번호를 붙인 것
    file_name=timeNow+'.csv' #file_name은 연-월-일_시분초.csv
    if cnt < file_limit:
        if not os.path.isdir('CSV_test\\test%d' %dir_num):
            os.mkdir('CSV_test\\test%d' %dir_num)
        nene_table.to_csv(dir_name + file_name, encoding="cp949", mode='w', index=True)
        #파일을 csv파일로 만들어주는 framework
        cnt = cnt + 1
        f=open('CSV_test\index.txt','w')
        f.write(str(cnt))
        f.close()
    #디렉터리에 파일이 3개까지 들어갈 수 있으므로 디렉터리 안에 파일 갯수가 3개 미만일 시,
    #test번호 디렉터리가 있다면 파일을 생성하여 적어주고, 없으면 생성.
    #index.txt는 현재 파일이 디렉터리에 몇 개 있는지 확인하므로 cnt를 증가시켜 적어준다.
        f=open('CSV_test\\dir_index.txt','w')
        f.write(str(dir_num))
        f.close()
        break
    #dir_index.txt에는 디렉터리가 몇 번 인지 적어준다.
    else:
        dir_num = dir_num+1
        cnt=0
        f=open('CSV_test\index.txt','w')
        f.write(str(cnt))
        f.close()
        #dir_num을 증가시키고 새로운 test 디렉터리에 index.txt를 생성
        #파일의 갯수를 적어준다
        f=open('CSV_test\\dir_index.txt','w')
        f.write(str(dir_num))
        f.close()
        continue
        #증가된 dir_num을 dir_index.txt에 적어주고 dir_num을 써준다.

print("stop")
#종료