import urllib.request
import datetime
import json
import re
import operator
# access_key="VNH7QeBnhzad%2B45QS4DMbIvJp0s%2Fx2iY9vdKxLYJJJEHMFFHDLr8HZJHuPgfjWRTg22OklmBOuSWznNeJktguQ%3D%3D"
access_key="aYk%2Fi2dkJ5CTB7ehuSJRPFPDwT3U96r25b%2B6MjwCrJJwGywnLR4qcln4%2BSR75IVpuNXbJLhrGiY2IedUR8A%2B4A%3D%3D"

def get_request_url(url):
    req=urllib.request.Request(url)

    try:
        response=urllib.request.urlopen(req)
        if response.getcode()==200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(),url))
        return None

def getNatVisitor(yyyymm,nat_cd,ed_cd):
    end_point='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    parameters="?_type=json&serviceKey=%s"%access_key
    parameters+="&YM="+yyyymm
    parameters+="&NAT_CD="+str(nat_cd)
    parameters+="&ED_CD="+str(ed_cd)
    url=end_point+parameters

    retData=get_request_url(url)
    if (retData==None):
        return None
    else:
        return json.loads(retData)

def main():
    with open('.\\national_code.txt','r',encoding='utf8') as infile :
        national_code_list=list(map(lambda x: x.rstrip().replace(' ',''), infile.readlines()))

    national_code_list[0]="000=미상"
    national_code_str=str(national_code_list)
    national_code_str=national_code_str[1:-1]
    national_code_str=national_code_str.replace('\'','').replace(',','').replace('=','')
    p=re.compile("(\d{3})([\w]*)\s")
    national_code_dic={}
    national_code_str_list=p.findall(national_code_str)
    for i in range(len(national_code_str_list)):
        national_code_dic[national_code_str_list[i][1]]=national_code_str_list[i][0]

    jsonResult=[]
    ed_cd='E'
    nStartYear=2017
    nEndYear=2018

    for year in range(nStartYear,nEndYear):
        for month in range(12,13):
            yyyymm="{0}{1:0>2}".format(str(year),str(month))
            for i in national_code_dic.values():
                national_code=str(i)
                jsonData=getNatVisitor(yyyymm,national_code,ed_cd)
                try:
                    if (jsonData['response']['header']['resultMsg']=='OK') :
                        krName= jsonData['response']['body']['items']['item']['natKorNm']
                        krName=krName.replace(' ','')
                        iTotalVisit=jsonData['response']['body']['items']['item']['num']
                        print('%s_%s:%s' %(krName,yyyymm,iTotalVisit))
                        jsonResult.append({'nat_name':krName,"nat_cd":national_code,'yyyymm':yyyymm,'visit_cnt':iTotalVisit})
                except:
                    print(national_code)
    cnVisit=[]
    VisitYM=[]

    i=0
    for item in jsonResult:
        VisitYM.append(item['yyyymm'])
        cnVisit.append(item['visit_cnt'])
    visit_rank={}
    for i in range (len(jsonResult)):
        try:
            visit_rank[jsonResult[i]['nat_name']]+=int(jsonResult[i]['visit_cnt'])
        except:
            visit_rank[jsonResult[i]['nat_name']]=int(jsonResult[i]['visit_cnt'])
    visit_rank_sorted=sorted(visit_rank.items(), key=operator.itemgetter(1),reverse=True)
    data_result=[]
    data_result.append(visit_rank_sorted)
    with open('ranking.json','w',encoding='utf8') as outfile :
        retJson= json.dumps(data_result,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)


if __name__=='__main__':
    main()











