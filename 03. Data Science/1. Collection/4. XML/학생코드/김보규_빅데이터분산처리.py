# XML_URL: http://nenechicken.com/subpage/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
# py -m pip install pandas
print("Start")
import urllib.request
from pandas import DataFrame
import os
import xml.etree.ElementTree as ET
import datetime
def save_nene():
    global dir_delimeter
    global top_dir
    global sub_dir
    dir_num=len(os.listdir('.'+dir_delimeter+top_dir+dir_delimeter))
    if len(os.listdir('.'+dir_delimeter+top_dir+dir_delimeter+sub_dir+str(dir_num))) ==3 :
        dir_num +=1
        os.mkdir('.'+dir_delimeter+top_dir+dir_delimeter+sub_dir+str(dir_num))
        nene_table.to_csv('.'+dir_delimeter+top_dir+dir_delimeter+sub_dir+str(dir_num)+dir_delimeter+nene_file+'.csv', encoding="utf8",mode='w',index=True)
    elif len(os.listdir('.'+dir_delimeter+top_dir+dir_delimeter+sub_dir+str(dir_num))) <3 :
        nene_table.to_csv('.'+dir_delimeter+top_dir+dir_delimeter+sub_dir+str(dir_num)+dir_delimeter+nene_file+'.csv', encoding="utf8",mode='w',index=True)


dir_delimeter='\\'
top_dir='V3_Bigdata'
sub_dir='nene'
nene_file=str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))



result = []
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])
if os.path.exists('.'+dir_delimeter+top_dir)==False:
    os.mkdir('.'+dir_delimeter+top_dir)
if os.path.exists('.'+dir_delimeter+top_dir+dir_delimeter+sub_dir+'1')==False :
    os.mkdir('.'+dir_delimeter+top_dir+dir_delimeter+sub_dir+'1')

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))
save_nene()
print("End")



