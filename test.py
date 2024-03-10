from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import re
import time


def check_language(received_txt):
    if re.search('[가-힣]', received_txt):
        return 'kor'
    elif re.search('[A-Za-z]', received_txt):
        return 'eng'
    else:
        return 0
        
        # 공통된 부분을 이용하여 작은 뉴스 제목과 작은 뉴스 제공사 추출
        #rso > div:nth-child(3) > div > g-section-with-header > div:nth-child(3) > a > div > div.SoAPf > div.MgUUmf.NUnG9d > span : 뉴스 제공사
        #rso > div:nth-child(3) > div > g-section-with-header > div:nth-child(5) > a > div > div.SoAPf > div.MgUUmf.NUnG9d > span
        
        #rso > div:nth-child(3) > div > g-section-with-header > div:nth-child(3) > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d : 뉴스 제목
        #rso > div:nth-child(3) > div > g-section-with-header > div:nth-child(5) > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d
        
        #rso > div:nth-child(3) > div > g-section-with-header > div:nth-child(3) > a > div > div.SoAPf > div.OSrXXb.rbYSKb.LfVVr > span : 경과 시간


def crawl_search_results(search_query, num_results=5):
    driver = webdriver.Chrome()

    # Google 검색 페이지로 이동
    driver.get('https://www.google.com')

    # 검색어 입력 영어, 한국어 구분
    search_box = driver.find_element(By.NAME, 'q')
    if check_language(str(search_query)) == 'kor':
        search_box.send_keys(search_query + " 뉴스")
    elif check_language(str(search_query)) == 'eng':
        search_box.send_keys(search_query + " news")
    else:
        print(f"What the fuck? :{search_box}")
    search_box.send_keys(Keys.RETURN)

    time.sleep(10) # 고작 이거 하나로 작동된다니
    
    # 검색 결과 페이지에서 뉴스 정보 추출
    news_info_list = []
    search_results = driver.find_elements(By.XPATH, '//*[@id="rso"]')

    for index, result in enumerate(search_results[:num_results], start=1):
        print(f"New total n : {len(search_results)}")
        # 뉴스 정보 추출
        title = result.find_element(By.CSS_SELECTOR, f'#rso > div:nth-child({index}) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > span').text

        # # 사이트 출처
        source = result.find_element(By.CSS_SELECTOR, f'#rso > div:nth-child({index}) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > div > div > div > div > cite').text

        # # 사이트 내용 (텍스트만 추출)
        content = result.find_element(By.CSS_SELECTOR, f'#rso > div:nth-child({index}) > div > div > div.kb0PBd.cvP2Ce.jGGQ5e > div > div > span > a > h3').text

        # # 업로드된 시간
        upload_time = result.find_element(By.CSS_SELECTOR, f'#rso > div:nth-child({index}) > div > div > div:nth-child(2) > div > span').text

        print(f"\n[ Site {index} ]")
        print(f"Title: {title}")
        print(f"Source: {source}")
        print(f"Content: {content}")
        print(f"Upload Time: {upload_time}")

        small_news_title = result.find_element(By.CSS_SELECTOR, '#rso > div:nth-child(3) > div > g-section-with-header > div:nth-child(3) > a > div > div.SoAPf > div.MgUUmf.NUnG9d > span').text
        small_news_provider = result.find_element(By.CSS_SELECTOR, '#rso > div:nth-child(3) > div > g-section-with-header > div:nth-child(3) > a > div > div.SoAPf > div.n0jPhd.ynAwRc.tNxQIb.nDgy9d').text

        print(f"{small_news_title} : {small_news_provider}")

        # 뉴스 정보를 리스트에 추가
        news_info_list.append({
            'Title': title,
            'Source': source,
            'Content': content,
            'Upload Time': upload_time,
            'Small News Title': small_news_title,
            'Small News Provider': small_news_provider
        })

    print(f"Top {num_results} search results for '{search_query}':")
    # for idx, news_info in enumerate(news_info_list, start=1):
    #     print(f"\nNews {idx}:")
    #     print(f"Title: {news_info['Title']}")
    #     print(f"Source: {news_info['Source']}")
    #     print(f"Content: {news_info['Content']}")
    #     print(f"Upload Time: {news_info['Upload Time']}")
    #     print(f"Small News Title: {news_info['Small News Title']}")
    #     print(f"Small News Provider: {news_info['Small News Provider']}")

    driver.quit()



# 사용자가 입력한 검색어로 검색 결과 크롤링 시작
search_query = input("Enter a search query: ")
crawl_search_results(search_query, num_results=10)
