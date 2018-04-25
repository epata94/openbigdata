import urllib.request
import os
import math
import datetime
from pandas import DataFrame

def make_dir():
    global dir_delimeter
    global dir_name
    os.mkdir('.'+dir_delimeter+dir_name)
def make_nene(dir_num):
    global dir_delimeter
    global dir_name
    global nene_dir
    os.mkdir('.'+dir_delimeter+dir_name+'\\'+nene_dir+dir_num)
def directory_num():
    global dir_delimeter
    global dir_name
    global nene_dir
    dir_num=len(os.listdir('.'+dir_delimeter+dir_name))
    while True:
        if len(os.listdir('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+str(dir_num))) == 3:
            dir_num+=1
            make_nene(str(dir_num))
        else : break
    return str(dir_num)

dir_name="V3_BigData"
dir_delimeter='\\'
nene_dir="Nene_Data"
nene_file=str(datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S'))
csv='csv'
record_limit=3

print("Start")
result = []
import xml.etree.ElementTree as ET
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root= ET.fromstring(xml)
for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])
nene_table= DataFrame(result,columns=('store','sido','gungu','store_address'))


if not os.path.exists('.'+dir_delimeter+dir_name) :
    make_dir()
if not os.path.exists('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+'1'):
    make_nene('1')

nene_table.to_csv('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+directory_num()+dir_delimeter+nene_file+'.'+csv,encoding='utf8',mode='w',index=True)
print("End")