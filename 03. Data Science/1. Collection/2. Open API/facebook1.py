import sys
import urllib.request
import json

page_name = "jtbcnews"
# app_id = "1494781874156708"
# app_secret = "b89ccfd79ef345a0e7921a2ae0f445c5"
app_id = "2012083495779336"
app_secret = "119bbb68efa94403cc17c2c3ecee4cdf"
access_token = app_id+"|"+app_secret

base = "https://graph.facebook.com/v2.8"
node = "/"+page_name
parameters="/?access_token=%s"%access_token

url=base+node+parameters

req = urllib.request.Request(url)
print("url: "+url)
try:
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        data = json.loads(response.read().decode('utf-8'))
        page_id = data['id']
        print("%s Facebook Numeric ID: %s"%(page_name,page_id))
except Exception as e:
    print(e)