import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
html = """<tbody>
a			
</tbody>
"""

soup=BeautifulSoup(html,'html.parser')
tags = soup.findall('tbody')
print("<soup>")
print(soup)
tags=soup.tbody
print("\ntag=soup.tbody")
print(tags)

sub_tag=tags.tr

print("\nsub_tag=tag.tr")
print(sub_tag)

tags = soup.findall('tbody')
print("\ntags = soup.findall('tbody')")
print(tags)
# tag=soup.a
# print(tag)
#
# print("\ntag.name")
# print(tag.name)
#
# print("\ntag.attrs")
# print(tag.attrs)
#
# print("tag.string")
# print(tag.string)
#
# print("tag.text")
# print(tag.text)