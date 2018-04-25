print("start")
import urllib.request
from pandas import DataFrame
import os
import time
import datetime

record_limit=3
result = []

if not os.path.isdir('V3_BigData'):
    os.mkdir('V3_BigData')

import xml.etree.ElementTree  as ET  # xml모듈을 가져오면서 xml.etree.ElementTree를 ET라는 새 이름으로 지정
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)#as ET가 없었다면 xml.etree.ElementTree.fromstring(..)으로
#했었어야 했음. 그마저도 변수 xml때문에 문제가 생김

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

Flag=0
count=0
folder_num = 1

# os.chdir("D:\Python_workspace\jump_to_python\Crawling\\01_10\\V3_BigData")
if not os.path.isdir('V3_BigData\\Nene_Data%d' %folder_num):
    os.mkdir('V3_BigData\\Nene_Data%d'%folder_num)

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))

################파일 인덱스
try:
    f=open('V3_BigData\index.txt','r')
    data=f.read()
    count=int(data)
    f.close()
except:
    f = open('V3_BigData\index.txt', 'w')
    f.write(str(count))
    f.close()
###################아래-폴더 인덱스
try:
    f=open('V3_BigData\\folder_index.txt','r')
    data=f.read()
    folder_num=int(data)
    f.close()
except:
    f = open('V3_BigData\\folder_index.txt', 'w')
    f.write(str(folder_num))
    f.close()

now=datetime.datetime.now()
nowDate=now.strftime('%Y-%m-%d')
Cnt_time=nowDate+'_'+time.strftime('%H%M%S')
#연월일 추가

while 1:
    folder_name = 'V3_BigData\\Nene_Data' + str(folder_num)+'\\'
    file_name = Cnt_time+ '.csv'
    if count < record_limit:
        # os.chdir("D:\Python_workspace\jump_to_python\Crawling\\01_10\\V3_BigData")
        if not os.path.isdir('V3_BigData\\Nene_Data%d' % folder_num):
            os.mkdir('V3_BigData\\Nene_Data%d' % folder_num)

        nene_table.to_csv(folder_name + file_name, encoding="cp949", mode='w', index=True)

        count += 1
        f = open('V3_BigData\index.txt', 'w')
        f.write(str(count))
        f.close()
        f = open('V3_BigData\\folder_index.txt', 'w')
        f.write(str(folder_num))
        f.close()
        break
    else:# 한 폴더당 최대 파일 갯수 초과시
        folder_num+=1
        count=0
        f = open('V3_BigData\index.txt', 'w')
        f.write(str(count))
        f.close()
        f = open('V3_BigData\\folder_index.txt', 'w')
        f.write(str(folder_num))
        f.close()
        continue

print("End")