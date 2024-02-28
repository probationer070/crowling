from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_top_sites(search_query):
    # 크롬 드라이버 경로 설정 (다운로드 받은 드라이버의 경로로 수정)
    # chrome_driver_path = '/crowling/chromedriver.exe'

    # 크롬 브라우저 열기
    driver = webdriver.Chrome()
    
    try:
        # 네이버 메인 페이지 열기 (예시로 네이버 사용)
        driver.get("https://www.naver.com/")

        # 검색어 입력
        search_box = driver.find_element(By.CSS_SELECTOR, 'input[name="query"]')
        search_box.send_keys(search_query)
        search_box.submit()
        
        
        contents = driver.find_elements(By.CSS_SELECTOR, 'body')
        # # 상단에 있는 사이트들의 링크를 가져오기
        # site_links = driver.find_elements(By.CSS_SELECTOR, '.group_nav > ul > li > a')
        
        # # 각 사이트에 접속하여 내용 스크래핑
        # for link in site_links[:5]:  # 상단 5개 사이트만 처리하도록 설정
        #     site_url = link.get_attribute("href")
        #     driver.get(site_url)
            
        #     # 각 사이트의 내용을 스크래핑하는 코드를 작성
        #     site_content = driver.find_element(By.TAG_NAME, 'body').text
        #     print(f"Site: {site_url}\nContent: {site_content}\n{'='*50}")

        #     # 일부 사이트는 JavaScript로 렌더링되므로, 필요에 따라 적절한 대기 시간을 추가할 수 있습니다.
        #     time.sleep(3)

    finally:
        # 브라우저 닫기
        driver.quit()

if __name__ == "__main__":
    search_query = input("검색할 단어를 입력하세요: ")
    scrape_top_sites(search_query)
