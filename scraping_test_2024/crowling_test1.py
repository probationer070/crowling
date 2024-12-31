# Web Crowling - 정적

import requests
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/worldstock/index/.INX/total"
html = requests.get(url).text

# print(html) # 연결 상태 정보 출력 text 제거해야 됨
print(html) # HTML 페이지 정보 출력

soup = BeautifulSoup(html, "html5lib")  # lxml의 형태로 정보 취득
# tags = soup.select_one("div.StockInfo_article__2fBr3 StockInfo_articleIndex__2H7fg")  # 특정 정보를 선택하여 가져옴
tags = soup.select("#text")

# datas = tags.select('ul > li > div > span')

# for data in datas:
#     print("[+] DATA : ",tag.get_text()) 
# print(tags)

