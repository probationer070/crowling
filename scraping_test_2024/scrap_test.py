from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup

import requests
import urllib
import re


def check_language(received_txt):
    if re.search('[가-힣]', received_txt):
        return 'kor'
    elif re.search('[A-Za-z]', received_txt):
        return 'eng'
    else:
        return 0

def crawl_search_results(search_query, num_results=5):

    # beautifulSoup 정적 크롤링 
    # keyword_fix = urllib.parse.quote(search_query)
    
    # base_url = f'https://news.google.com/rss/search?q={keyword_fix}&hl=ko&gl=KR&ceid=KR%3Ako'
    # response = requests.get(base_url)

    # if response.status_code == 200:
    #     print("[+] Access Granted \n")
    #     # print(response.text) # 전체 스크립트 출력
        
    #     soup = BeautifulSoup(response.text, 'xml') 
        
    #     news_list = soup.find_all('item')[:num_results]
                
    #     for index, news in enumerate(news_list, start=1):
    #         try:
    #             upload_time = news.find('pubDate').text
    #         except AttributeError:
    #             upload_time = news.find('pubdate').text
            
    #         news_title = news.find('title').text
    #         news_url = news.find('link').text
    #         print(f"Upoladed time [{upload_time}] ")
    #         print(f"{index}. {news_title}")
    #         print(f"Link : {news_url}\n")

    # else:
    #     print(f"[-] Access Denied, Status code : {response.status_code}")
        
    # -----------------------------------------------------
        
        
        
        

    # 동적 크롤링 (Selenium)
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    
    # 검색어 입력 영어, 한국어 구분
    # search_box = driver.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')
    search_box = driver.find_element(By.NAME, 'q')
    
    if check_language(str(search_query)) == 'kor':
        search_box.send_keys(search_query+" 뉴스")
    
    elif check_language(str(search_query)) == 'eng':
        search_box.send_keys(search_query+" news")
        
    else:
        print(f"What the fuck? :{search_box}")
    search_box.send_keys(Keys.RETURN)
    
    # Google 검색 페이지로 이동
    

    

    search_result_url = driver.current_url
    print(f"검색 결과 페이지 URL: {search_result_url}")
    contents = driver.find_elements(By.CSS_SELECTOR, 'body')
        
    # 페이지의 HTML 코드 가져오기
    page_html = driver.page_source
    
     # 검색 결과 스크랩
    sites = driver.find_elements(By.XPATH, '//*[@id="rso"]')[:num_results]
    
     # 페이지 최상단 검색 결과
    site_name = sites[0].find_element(By.XPATH, '//*[@id="rso"]/div/div/div[1]/div/div/a/div/div[2]/div[2]').text # span.VuuXrf
    # site_url = sites[0].find_element(By.CSS_SELECTOR, '#rso > div > div > div:nth-child(1) > div > div > a > div > div.SoAPf > div.OSrXXb.rbYSKb.LfVVr').text # cite.qLRx3b.tjvcx.GvPZzd.cHaqb
    # site_topic = sites[0].find_element(By.CSS_SELECTOR, '#rso > div > div > div:nth-child(1) > div > div > a > div > div.SoAPf > div.n0jPhd.ynAwRc.MBeuO.nDgy9d').text # h3.LC20lb.MBeuO.DKV0Md
    # site_info = sites[0].find_element(By.CSS_SELECTOR, '#rso > div > div > div:nth-child(1) > div > div > a > div > div.SoAPf > div.GI74Re.nDgy9d').text # div.VwiC3b.yXK7lf.lVm3ye.r025kc.hJNv6b.Hdw6tb
            
    # if len(sites) <= num_results:
    #     for i in range(num_results - len(sites)):
    #         sites.append(driver.find_elements(By.CSS_SELECTOR, f'#rso > div:nth-child(3) > div:nth-child({1})')[0])
    #         print(f"[+] total sites : {len(sites)}")
    #         print(sites, "\n")

    #         # 페이지 최상단 검색 결과
    #         site_name = sites[i].find_element(By.CSS_SELECTOR, '').text # span.VuuXrf
    #         site_url = sites[i].find_element(By.CSS_SELECTOR, '').text # cite.qLRx3b.tjvcx.GvPZzd.cHaqb
    #         site_topic = sites[i].find_element(By.CSS_SELECTOR, '').text # h3.LC20lb.MBeuO.DKV0Md
    #         site_info = sites[i].find_element(By.CSS_SELECTOR, '').text # div.VwiC3b.yXK7lf.lVm3ye.r025kc.hJNv6b.Hdw6tb
            
    #         print(f"[ Site {1} ]")
    #         print(f"Name: {site_name}")
    #         print(f"URL: {site_url}")
    #         print(f"Topic: {site_topic}")
    #         print(f"Info: {site_info}")
    
    for result in search_results[:num_results]:
        news_link = result.get_attribute('href')
        driver.get(news_link)

        # Selenium이 페이지가 완전히 로드될 때까지 대기
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//h1')))

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # 뉴스 정보 추출
        news_title = soup.find('h1').text.strip()

        # 공통된 부분을 이용하여 작은 뉴스 제목과 작은 뉴스 제공사 추출
        small_news_title = soup.select_one('div.vu9Nlb.HdAYZc a div.MgUUmf.NUnG9d').text.strip()
        small_news_provider = soup.select_one('div.vu9Nlb.HdAYZc a div.MgUUmf.NUnG9d').text.strip()

        # 뉴스 정보를 리스트에 추가
        news_info_list.append({
            'Link': news_link,
            'Title': news_title,
            'Small News Title': small_news_title,
            'Small News Provider': small_news_provider
        })
    
    
    # 검색 결과 출력
    print(f"Top {num_results} search results for '{search_query}':")
    for idx, news_info in enumerate(news_info_list, start=1):
        print(f"\nNews {idx}:")
        print(f"Title: {news_info['Title']}")
        print(f"Link: {news_info['Link']}")
        print(f"Summary: {news_info['Summary']}")
        print(f"Upload Date: {news_info['Upload Date']}")

    driver.quit()

# 사용자가 입력한 검색어로 검색 결과 크롤링 시작
search_query = input("Enter a search query: ")
crawl_search_results(search_query, num_results=5)
