import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET
import time

print('Start')

result = []
dir_name = "V3_Bigdata"
dir_parameter = "\\"
nene_dir = "nene"
nene_file = str(time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time())))
csv = ".csv"

def search_nene_dir():
    global count_dir
    count_dir = len(os.listdir('.' + dir_parameter + dir_name))

def search_nene_file(count_dir):
    global count_file
    count_file = len(os.listdir('.' + dir_parameter + dir_name + dir_parameter + nene_dir+str(count_dir)))

def make_nene_dir(index):
    os.mkdir(dir_name + dir_parameter + nene_dir+str(index))

def make_nene_file(dir_index):
    file_csv = dir_name + dir_parameter + nene_dir+str(dir_index) + dir_parameter + nene_file + csv
    nene_table.to_csv(file_csv, encoding="utf8", mode='w', index=True)

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('utf8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

    nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))

try: os.mkdir(dir_name)
except: pass
try:
    search_nene_dir()
    search_nene_file(count_dir)
    if count_file < 3:
        make_nene_file(count_dir)
    else:
        count_dir += 1
        make_nene_dir(count_dir)
        make_nene_file(count_dir)
except:
    make_nene_dir(1)
    make_nene_file(1)

print('End')