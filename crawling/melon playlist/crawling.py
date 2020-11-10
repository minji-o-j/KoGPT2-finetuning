# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome('/Users/user/Desktop/chromedriver')
driver.implicitly_wait(3) # 암묵적으로 웹 자원 로드를 위해 10초까지 기다려 준다.
## 아이돌 태그 플레이리스트 이름 받아오기=====================================================
idol_page=[]
i=1
while i<=1861:
    idol_page.append(i)
    i+=20
#print(idol_page)
idolurl="https://www.melon.com/dj/tag/djtaghub_list.htm?tagSeq=125#params%5BtagSeq%5D=125&params%5BorderBy%5D=POP&po=pageObj&startIndex="
playlist=[]

for i in idol_page:
    idolurl_page=idolurl+str(i)
    driver.get(idolurl_page)
    html = driver.page_source
    soup1 = bs(html,'html.parser')
    ply_name=soup1.find_all('div',class_='entry')

    for ply in ply_name:
        playlist.append(ply.find('a',class_='ellipsis album_name').text.translate({ ord('\n'): '',ord('\t'): '',ord('\r'): '' })) #앞뒤로 붙어있던 공백들 제거
     
## 댄스 태그 플레이리스트 이름 받아오기=====================================================
dance_page=[]
i=1
while i<=21:
    dance_page.append(i)
    i+=20 
danceurl="https://www.melon.com/dj/tag/djtaghub_list.htm?tagSeq=29#params%5BtagSeq%5D=29&params%5BorderBy%5D=POP&po=pageObj&startIndex="

for i in dance_page:
    danceurl_page=danceurl+str(i)
    driver.get(danceurl_page)
    html = driver.page_source
    soup1 = bs(html,'html.parser')
    ply_name=soup1.find_all('div',class_='entry')

    for ply in ply_name:
        playlist.append(ply.find('a',class_='ellipsis album_name').text.translate({ ord('\n'): '',ord('\t'): '',ord('\r'): '' })) #앞뒤로 붙어있던 공백들 제거
 

## 엑셀로 저장=====================================================
data = pd.DataFrame(playlist)
data.columns = ['playlist']
data=data.drop_duplicates("playlist", keep="first")
data.to_csv('playlist_tag_idol.csv',encoding='utf-8-sig')




