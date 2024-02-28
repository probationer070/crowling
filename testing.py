import requests
import urllib
import time

from bs4 import BeautifulSoup
from selenium import webdriver

class Test:
    def __init__(self, keyword):
        self.keyword = keyword 

    @staticmethod
    def loading_animation(response, option="cli_ver_simple_bar"):
        
        if option == "cli_ver_simple_bar":
            while True:
                for symbol in "\\|/-":
                    print(f"\rSearching {symbol}", end="", flush=True)
                    time.sleep(0.1)
                    # 여기에 다음 출력을 확인하는 로직을 추가
                    if response.status_code == 200:
                        return "\n"
                    
        elif option == "cli_ver_simple_dot":
            while True:
                for i in range(0, 4):
                    dots = "." * i
                    spaces = " " * (4 - i)
                    print(f"\rSearching{dots}{spaces}", end="", flush=True)
                    time.sleep(0.5)
                    # 여기에 다음 출력을 확인하는 로직을 추가
                    if response.status_code == 200:
                        return "\n"
        else:
            print("\n Invalid options \n")

    def crawl_google_news_titles(self, num_results=5):
        keyword_fix = urllib.parse.quote(self.keyword)
        base_url = f'https://news.google.com/rss/search?q={keyword_fix}&hl=ko&gl=KR&ceid=KR%3Ako'

        response = requests.get(base_url)
        Test.loading_animation(response, option="cli_ver_simple_bar")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'xml')
            items = soup.find_all('item')[:num_results]

            for index, item in enumerate(items, start=1):
                title = item.find('title').text
                print(f"\n{index}. {title}")

        else:
            print(f"Failed to fetch Google News. Status code: {response.status_code}")

        return str(response)


if __name__ == "__main__":
    keyword_input = input("[ What you want to find ] : ")
    test_instance = Test(keyword_input)
    test_instance.crawl_google_news_titles(num_results=5)
    
# 해당 코드는 상당히 비효율적이다
