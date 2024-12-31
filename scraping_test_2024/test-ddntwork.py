from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup

import re
import time


def check_language(received_txt):
    if re.search('[가-힣]', received_txt):
        return 'kor'
    elif re.search('[A-Za-z]', received_txt):
        return 'eng'
    else:
        return 0

def crawl_search_results(search_query, num_results=5):
    chrome_service = webdriver.ChromeService(executable_path='chromedriver.exe')
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')        #창이 나타나지 않도록 Headless설정하기
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('user-agent=' + user_agent)

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    # Google 검색 페이지로 이동
    driver.get('https://news.google.com/rss/search?q='+search_query)  # rss 기준

    # 검색어 입력 영어, 한국어 구분 - 구글 일반 검색 기준
    # search_box = driver.find_element(By.NAME, 'q')
    # if check_language(str(search_query)) == 'kor':
    #     search_box.send_keys(search_query + " 뉴스")
    # elif check_language(str(search_query)) == 'eng':
    #     search_box.send_keys(search_query + " news")
    # else:
    #     print(f"What the fuck? :{search_box}")
    # print(search_box)
    # search_box.send_keys(Keys.RETURN)

    # time.sleep(100) # 고작 이거 하나로 작동된다니
    
    # 검색 결과 페이지에서 뉴스 정보 추출
    news_info_list = []
    search_results = driver.find_element(By.XPATH, '//*[@id="folder1"]')

    # print(search_results.text)
    search_results = re.sub("<item>|</item>", " ", str(search_results.text))
    search_results_list = search_results.split("  ")
    print(search_results_list)
    print(f"New total n : {len(search_results_list)}")
    for index, result in enumerate(search_results[:num_results], start=2):
        
        # 뉴스 제목
        title = result.find_element(By.XPATH, f'//*[@id="folder{index}"]/div[2]/div[1]/span[2]').text

        # 사이트 링크
        source = result.find_element(By.XPATH, f'//*[@id="folder{index}"]/div[2]/div[2]/span[2]').text
        
        # 사이트 출처
        content = result.find_element(By.XPATH, f'//*[@id="folder{index}"]/div[2]/div[6]/span[2]').text
        
        # 업로드된 시간
        upload_time = result.find_element(By.XPATH, f'//*[@id="folder{index}"]/div[2]/div[4]/span[2]').text

        print(f"\n[ Site {index} ]")
        print(f"Title: {title}")
        print(f"Source: {source}")
        print(f"Content: {content}")
        print(f"Upload Time: {upload_time}")

    driver.quit()



# 사용자가 입력한 검색어로 검색 결과 크롤링 시작
search_query = input("Enter a search query: ")
crawl_search_results(search_query, num_results=10)
