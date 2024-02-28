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
        
        # elem = driver.find_element(By.NAME, 'body')  # Find the search box
        contents = driver.find_elements(By.CSS_SELECTOR, 'body')
        print(contents.text)

    finally:
        # 브라우저 닫기
        driver.quit()

if __name__ == "__main__":
    search_query = input("검색할 단어를 입력하세요: ")
    scrape_top_sites(search_query)


#---------------------------------------------------------------


    try:
        # 네이버 홈페이지 열기
        driver.get("https://www.naver.com/")

        # 검색어 입력
        search_box = driver.find_element_by_name("query")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # 검색 후의 URL 출력
        search_result_url = driver.current_url
        print(f"검색 결과 페이지 URL: {search_result_url}")

        # 일부 사이트는 JavaScript로 렌더링되므로, 필요에 따라 적절한 대기 시간을 추가할 수 있습니다.
        time.sleep(3)

        # 현재 페이지의 HTML 본문 출력
        html_content = driver.page_source
        print(f"\nHTML 본문:\n{html_content}")

    finally:
        # 브라우저 닫기
        driver.quit()

if __name__ == "__main__":
    search_query = input("검색할 단어를 입력하세요: ")
    naver_search_and_print_html(search_query)
