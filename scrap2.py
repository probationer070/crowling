from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_top_sites(search_query):
    # 크롬 브라우저 열기
    driver = webdriver.Chrome()
    
    try:
        # 네이버 메인 페이지 열기 (예시로 네이버 사용)
        driver.get("https://www.naver.com/")

        # 검색어 입력
        search_box = driver.find_element(By.CSS_SELECTOR, 'input[name="query"]')
        search_box.send_keys(search_query)
        search_box.submit()
        
        search_result_url = driver.current_url
        print(f"검색 결과 페이지 URL: {search_result_url}")
        # elem = driver.find_element(By.NAME, 'body')  # Find the search box
        contents = driver.find_elements(By.CSS_SELECTOR, 'body')
        print(driver.page_source)   # 해당 페이지의 소스 보여줌

    finally:
        # 브라우저 닫기
        driver.quit()

if __name__ == "__main__":
    search_query = input("검색할 단어를 입력하세요: ")
    scrape_top_sites(search_query)


#---------------------------------------------------------------
