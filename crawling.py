# -*- coding: utf-8 -*-

from urllib.request import urlopen, Request
import urllib
import bs4
from bs4 import BeautifulSoup as bs
import requests
import re
##페이지 정보 받아오기==============================================================
idol_page=[]
i=21
while i<=1861:
    idol_page.append(i)
    i+=20
#print(idol_page)
idolurl="https://www.melon.com/dj/tag/djtaghub_list.htm?tagSeq=125#params%5BtagSeq%5D=125&params%5BorderBy%5D=POP&po=pageObj&startIndex="
playlist=[]
idolurl_page=idolurl+str(21)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
c_idolurl=requests.get(idolurl_page,headers=header)
soup1 = bs(c_idolurl.text,'html.parser')
#print(soup1)
ply_name=soup1.find_all('div',class_='entry')

for ply in ply_name:
    playlist.append(ply.find('a',class_='ellipsis album_name').text.translate({ ord('\n'): '',ord('\t'): '',ord('\r'): '' })) #앞뒤로 붙어있던 공백들 제거       
'''
for i in idol_page:
    idolurl_page=idolurl+str(idol_page[1])
    print(idolurl_page)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
    c_idolurl=requests.get(idolurl_page,headers=header)
    soup1 = bs(c_idolurl.text,'html.parser')
    #print(soup1)
    ply_name=soup1.find_all('div',class_='entry')
    
    for ply in ply_name:
        playlist.append(ply.find('a',class_='ellipsis album_name').text.translate({ ord('\n'): '',ord('\t'): '',ord('\r'): '' })) #앞뒤로 붙어있던 공백들 제거
'''        
print(playlist)
