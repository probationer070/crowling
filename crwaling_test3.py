import requests
import urllib
from bs4 import BeautifulSoup

# 브라우저의 통신 방법이 Ajax로 변경되서 html 파싱이 아닌 다른 방식으로 크롤링
# Ajax에서 불러오는 json을 이용 + url 주소에 rss를 첨가하여 데이터만 피드 받도록 함

def crawl_the_data(keyword, num_stated=10):
    
    print("[ What did you find ] : ",keyword, "\n")
    keyword_fix = urllib.parse.quote(keyword)   # 특수문자 URL 인코딩 안하면 다른 값으로 전달됨 -> 인코딩 해줌
    
    base_url = f'https://news.google.com/rss/search?q={keyword_fix}&hl=ko&gl=KR&ceid=KR%3Ako'

    # HTTP GET 요청
    response = requests.get(base_url)
    
    if response.status_code == 200:
        print("[+] Access Granted \n")
        # print(response.text) # 전체 스크립트 출력
        
        soup = BeautifulSoup(response.text, 'lxml') # XML 파일이라고 생각해서 했는데 왜 자꾸 경고문이 뜨는지 모르겠음 ?
        
        news_list = soup.find_all('item')[:num_stated]
                
        for index, news in enumerate(news_list, start=1):
            upload_time = news.find('pubdate').text
            news_title = news.find('title').text
            print(f"{index}. {news_title} : Upoladed time [{upload_time}] ")

    else:
        print(f"[-] Access Denied, Status code : {response.status_code}")


crawl_the_data("S&P500", num_stated=5)