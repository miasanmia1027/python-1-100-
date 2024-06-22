from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys
import requests
import io
# -*- coding: utf-8 -*-



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#한글깨짐을 고치기 위한 방법2




web_url=webdriver.Chrome()

url="https://namu.wiki/w/Project%20Zomboid/%EC%95%84%EC%9D%B4%ED%85%9C"

web_url.get(url)
#Q=get 와 requsts(import requeesst__외부라이브러리)의 차이점은
#A=

get_screen_height=web_url.execute_script("return window.screen.height;")#이렇게 해서 원도우의 높이를 가져오기
#Q=이게 왜 필요할가?
#A=

soup = BeautifulSoup(web_url.page_source, "html.parser",from_encoding='cp949')#html의 모든것을 가져온다
#,from_encoding='cp949'이부분은 한글깨짐으 고치기 위한 방법1


text_download=[]
i=1
while True:
    i+=1
    #과연 여기에 time.sleep이 필요할까?
   
    web_url.execute_script(f"window.scrollTo(0, {get_screen_height * i});")

    #find_tittle = soup.find('span', {'class':" style-scope ytd-compact-video-renderer style-scope ytd-compact-video-renderer"})

    
    
    
    
    
    for div in soup('div') : # div 안의
        for div in div('div') : # div 태그 중에서
            if ('class' in div.attrs # div가 class 속성을 가지고 있고
                and 'IFc0jZrc' in div['class']): # class가 'pLZXahO9'이다
                every_text=div.get_text()
                
                
                # 찾고자 하는 텍스트
                target_text = "::marker"
                
                # 텍스트가 포함된 부분을 제거
                if target_text in every_text:
                    every_text = every_text.replace(target_text, '')
                
                
                text_download.append(every_text)
                
                
    
                        
    
    
    
    
    
    all_of_bodt_hight= web_url.execute_script("return document.body.scrollHeight;")#<body>의 길이 즉 전체 길이를 확인하기 위한것


    if all_of_bodt_hight<=get_screen_height*i:#만약에 스크롤 하는 <body>의 범위를 벗어났을때 적당히 하라는것
        break

#여기까지가 페이지를 밑에까지 스크롤 하는 과정

#get_source =web_url.page_source 
#print(get_source)#이것들은 html의 모든것을 가져오는것












#with open('text.txt', 'a') as file:
    #file.write(name)


#output_file = 'test.html'
#with open(output_file, 'w', encoding='utf-8') as file:
   # file.write(soup.prettify())



import sys
 
# Save the original stdout
original_stdout = sys.stdout
 
# Redirect stdout to a file
with open('where i want.txt', 'w') as f:
    sys.stdout = f
    print(text_download)
 