import requests
import urllib
# import searching

from bs4 import BeautifulSoup
from selenium import webdriver


class test:
    def __init__(self, keyword):
        self.keyword = keyword 

    def crawl_google_news_titles(keyword, num_results=5):
        
        # print(searching.loading_animation() ,keyword)
        keyword_fix = urllib.parse.quote(keyword)
        
        
        base_url = f'https://news.google.com/rss/search?q={keyword_fix}&hl=ko&gl=KR&ceid=KR%3Ako'
        
        response = requests.get(base_url)
        print(response)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'xml')

            items = soup.find_all('item')[:num_results]

            for index, item in enumerate(items, start=1):
                title = item.find('title').text
                print(f"{index}. {title}")

        else:
            print(f"Failed to fetch Google News. Status code: {response.status_code}")

# 특정 키워드로 Google 뉴스 제목만 크롤링
test.crawl_google_news_titles(input("[ What you want find ] : "), num_results=5)
