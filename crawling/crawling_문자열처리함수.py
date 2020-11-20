# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import re
driver = webdriver.Chrome('/Users/308_2/minji/chromedriver')
driver.implicitly_wait(8) # 암묵적으로 웹 자원 로드를 위해 8초까지 기다려 준다.
## 아이돌 태그 플레이리스트 이름 받아오기=====================================================
page=[]
i=1
while i<=9981: #9981 이후로 안불러와짐(실제로)
    page.append(i)
    i+=20
playlist=[]
for i in range(2,46986): #tag 2~46985까지 있었음
    url="https://www.melon.com/dj/tag/djtaghub_list.htm?tagSeq="+str(i)+"#params%5BtagSeq%5D="+str(i)+"&params%5BorderBy%5D=POP&po=pageObj&startIndex="
    for j in page:
        url_page=url+str(j)
        driver.get(url_page)
        html = driver.page_source
        soup1 = bs(html,'html.parser')
        ply_name=soup1.find_all('div',class_='entry')
        if(len(ply_name)==0):
            break;
        for ply in ply_name:
            ply_delete=ply.find('a',class_='ellipsis album_name').text.translate({ ord('\n'): '',ord('\t'): '',ord('\r'): '' })#앞뒤로 붙어있던 공백들 제거
            
            # 플레이리스트 이름이 너무 많기 때문에 공백을 제외하고 특수문자가 있는 경우는 아예 list에 포함시키지 않을 예정
            # R&B같은 경우 &과 같은 특수문자를 없애 버리면 생성에 어려움을 겪을 것으로 예상하여 아예 추가하지 않을 것임
            delete_space=ply_delete.translate({ ord(' '): ''})
            
            if(delete_space.isalnum()):#문자열만 있는것이 True일 경우에만
                playlist.append(ply_delete)
## 엑셀로 저장=====================================================
data = pd.DataFrame(playlist)
data.columns = ['playlist']
data=data.drop_duplicates("playlist", keep="first")
data.to_csv('playlist_list.csv',encoding='utf-8-sig')




