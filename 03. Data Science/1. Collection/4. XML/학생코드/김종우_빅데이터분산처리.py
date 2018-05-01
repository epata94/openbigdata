# XML_URL: http://nenechicken.com/subpage/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
# py -m pip install pandas
print("Start")
import urllib.request
import os
import datetime
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []

now = datetime.datetime.now()
nowTime = now.strftime('%Y-%m-%d_%H%M%S')

dir_name="V3_Bigdata"
dir_delimeter="\\"
nene_dir="nene"
nene_file=nowTime
csv=".csv"
file_limit = 3

def make_dir(index):
    os.mkdir(dir_name + dir_delimeter + nene_dir + str(index))
    return None
def make_file(dir_index, file_index):
    nene_csv = dir_name+dir_delimeter+ nene_dir + str(dir_index) + dir_delimeter + nene_file + csv;

    nene_table.to_csv(nene_csv, encoding="cp949", mode='w', index=True)
    return None


response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))



try:
    os.mkdir(dir_name)
except: pass

try:
    with open(dir_name + dir_delimeter + "index_nene.txt" , 'r') as file:
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = int(file_index/file_limit)
        if file_index%file_limit != 0:
            dir_index = dir_index + 1
        if file_index%file_limit == 1:
            make_dir(dir_index)

        make_file(dir_name, file_index)
        file_limit +=1
    with open(dir_name + dir_delimeter + "index_nene.txt", 'w') as file:
        file.write(str(file_index))

except FileNotFoundError:
    with open(dir_name + dir_delimeter + "index_nene.txt", 'w') as file:
        file.write('2')
    make_dir(1)
    make_file(1,1)



